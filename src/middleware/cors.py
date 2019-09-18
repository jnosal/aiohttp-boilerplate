from aiohttp import web


@web.middleware
async def cors_middleware(request, handler):
    response = await handler(request)
    response.headers.update({
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET,HEAD,OPTIONS,POST,PUT,DELETE,PATCH',
        'Access-Control-Allow-Headers': (
            'Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, '
            'Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers'
        ),
        'Access-Control-Allow-Credentials': 'true'
    })
    return response
