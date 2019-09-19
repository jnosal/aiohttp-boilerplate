from aiohttp import web

from . import settings
from src.app import init_app


async def create_app():
    """
        Application factory used by gunicorn
    """
    app = init_app()
    return app


def main():
    """
        Standalone server startup script
    """
    app = init_app()

    web.run_app(
        app,
        host=settings.HOST,
        port=settings.PORT,
    )


if __name__ == '__main__':
    main()
