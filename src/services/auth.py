import abc
import functools

import aiohttp.web
import jwt


PARAM_API_KEY = 'api_key'


class BaseAuthentication(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    async def authenticate(self, *args, **kwargs):  # pragma: no cover
        pass

    @abc.abstractmethod
    async def get_user(self, identifier):  # pragma: no cover
        pass


class JWTAuthentication(BaseAuthentication):

    def _encode(self, **kwargs):
        return jwt.encode(
            kwargs, settings.JWT_SECRET, settings.JWT_ALGORITHM
        ).decode('utf-8')

    def _decode(self, identifier):
        try:
            return jwt.decode(
                identifier, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            pass

    async def get_token(self, **kwargs):
        return self._encode(**kwargs)

    async def get_user(self, identifier):
        client = tw.TWAPIClient()

        payload = self._decode(identifier)
        if not payload:
            return

        auth_token = payload.get('auth_token')
        player_id = payload.get('player_id')

        user = await client.user_details(
            auth_token=auth_token, player_id=player_id)

        return user

    async def authenticate(self, *args, **kwargs):
        client = tw.TWAPIClient()

        return await client.user_sign_in(
            email=kwargs['email'], password=kwargs['password'])


def auth_required(func):
    func.__auth_required__ = True

    def get_authentication_service(request):
        return request.app['auth']

    @functools.wraps(func)
    async def _required(*args):
        view = args[-1]
        request = view.request
        token = request.headers.get('Authorization')

        if not token:
            raise aiohttp.web.HTTPForbidden()

        service = get_authentication_service(request)
        user = await service.get_user(token)

        if user is None:
            raise aiohttp.web.HTTPForbidden()

        request.user = user
        return await func(*args)

    return _required


def api_key_required(func):
    func.__api_key_required__ = True

    @functools.wraps(func)
    async def _required(*args):
        view = args[-1]
        request = view.request
        api_key = request.headers.get('Authorization')

        if not api_key == settings.INTERNAL_API_KEY:
            raise aiohttp.web.HTTPForbidden()

        return await func(*args)

    return _required
