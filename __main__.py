from aiohttp import web

from src import create_app

web.run_app(
    create_app(), port=3000
)
