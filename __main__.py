from aiohttp import web

from src.core import create_app

web.run_app(
    create_app(), port=3000
)
