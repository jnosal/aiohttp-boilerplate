import logging

from aiohttp import web, web_exceptions


@web.middleware
async def error_middleware(request, handler):
    try:
        return await handler(request)
    except web_exceptions.HTTPNotFound:
        return web.json_response({}, status=404)
    except Exception as e:
        logging.error(e, exc_info=True)
        raise
