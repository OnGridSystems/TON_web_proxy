import aiohttp_jinja2

from aiohttp import web

from src.settings import PROXY_SERVER_ADDRESS, PROXY_SERVER_PORT
from src.utils.request_proxy import profixy_request
from src.utils.url_parse import parse_url


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


@route_web_proxy.get('/*')
async def wild_card(request: web.Request) -> web.Response:
    path = 'http://test.ton'
    print(request.path)
    await profixy_request(path)


@route_web_proxy.post('/api/request')
async def request_ton_site(request: web.Request) -> web.Response:
    print(
        f'Incoming request < [{request.method}] > '
        f'from: {request.host}{request.path}'
    )
    request_body: dict = await request.json()
    # raw_url: ParseResult = urlparse()
    url: str = parse_url(request_body['path'])
    print(f'Parsed URL: {url}')
    if len(url) != 0:
        return await profixy_request(url, target_url)
    else:
        return web.Response(
            text=(
                'You are requested an empty address!'
            ),
            status=404
        )
