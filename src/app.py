from aiohttp import web
from src.handlers.status import StatusView
from src import middleware


def init_app():
    app = web.Application(
        debug=True,
        middlewares=[
            middleware.cors_middleware,
            middleware.error_middleware
        ]
    )
    app.router.add_view('/status', StatusView)
    return app
