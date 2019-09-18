from aiohttp import web
from .app import init_app


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
    app_settings = app['config']['app']

    web.run_app(
        app,
        host=app_settings['host'],
        port=app_settings['port'],
    )


if __name__ == '__main__':
    main()
