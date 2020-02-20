import aiohttp
import aiohttp_jinja2

from aiohttp import web

from src.settings import PROXY_SERVER_ADDRESS, PROXY_SERVER_PORT

route_web_proxy = web.RouteTableDef()


@route_web_proxy.get('/')
async def index_ton_proxy(request: web.Request) -> web.Response:
    print(
        f'Incoming request < [{request.method}] > '
        f'from: {request.host}{request.path}'
    )
    context = {}
    response = aiohttp_jinja2.render_template(
        'templates/base_layout.html',
        request,
        context
    )
    return response


@route_web_proxy.post('/api/request')
async def request_ton_site(request: web.Request) -> web.Response:
    print(
        f'Incoming request < [{request.method}] > '
        f'from: {request.host}{request.path}'
    )
    target_url = (
        f'http://{PROXY_SERVER_ADDRESS}:{PROXY_SERVER_PORT}'
    )
    request_body = await request.json()
    path = request_body['path']
    print(f'Target URL: {target_url}')
    print(f'Target PATH: {path}')
    if 'http' or 'https' not in path:
        path = f'http://{path}'
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    path, proxy=target_url) as response:
                raw_response = await response.text(encoding='utf-8')
            return web.Response(
                body=raw_response,
                status=response.status,
                headers={
                    'Content-Type': 'text/html',
                    'Referer': target_url
                }
            )
    elif 'http' or 'https' in path:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    path, proxy=target_url, timeout=30) as response:
                raw_response = await response.text(encoding='utf-8')
            return web.Response(
                body=raw_response,
                status=response.status,
                headers={
                    'Content-Type': 'text/html',
                    'Referer': target_url
                }
            )
    else:
        return web.Response(
            text='You have been sent some shit to me, damn!',
            status=404
        )
