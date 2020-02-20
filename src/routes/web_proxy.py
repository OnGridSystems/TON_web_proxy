import aiohttp
import aiohttp_jinja2
from aiohttp import web

from src.settings import PROXY_SERVER_ADDRESS, PROXY_SERVER_PORT

route_web_proxy = web.RouteTableDef()

target_url = f'http://{PROXY_SERVER_ADDRESS}:{PROXY_SERVER_PORT}'


@route_web_proxy.get('/')
async def index_ton_proxy(request: web.Request) -> web.Response:
    print(
        f'Incoming request < [{request.method}] > '
        f'from: {request.host}{request.path}'
    )
    context = {}
    response = aiohttp_jinja2.render_template(
        'templates/base_layout.html', request, context
    )
    return response


@route_web_proxy.post('/api/request')
async def request_ton_site(request: web.Request) -> web.Response:
    print(
        f'Incoming request < [{request.method}] > '
        f'from: {request.host}{request.path}'
    )
    request_body = await request.json()
    path = request_body['path']
    if len(path) != 0:
        if 'http' or 'https' not in path:
            path = f'http://{path}'
            return await profixy_request(path)

        elif 'http' or 'https' in path:
            return await profixy_request(path)

        else:
            return web.Response(
                text=(
                    'Wrong request! ' f'Try to to use with proto: http://{path}'
                ),
                status=404,
            )
    else:
        return web.Response(
            text=(
                'You are requested an empty address!'
            ),
            status=404
        )


async def profixy_request(path):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(path, proxy=target_url, timeout=30) as response:
                raw_response = await response.text(encoding='utf-8')
                print(f'Proxifying request of "{path}"')
            return web.Response(
                body=raw_response,
                status=response.status,
                headers={'Content-Type': 'text/html', 'Referer': target_url},
            )
    except Exception as err:
        return web.Response(
            text=f'Occurred error while requesting specified address: "{path}"'
                 f'Error context: {err.__context__}',
            status=400
        )
