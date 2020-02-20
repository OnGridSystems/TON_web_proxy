import jinja2
import aiohttp_jinja2

from aiohttp import web

from src.core.middlewares import cors_middleware
from src.routes import route_web_proxy


def create_app():
    app = web.Application(middlewares=[cors_middleware])
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(
            './frontend/'
        )
    )
    app.add_routes(route_web_proxy)

    return app
