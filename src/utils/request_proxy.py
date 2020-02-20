import aiohttp

from aiohttp import web


async def profixy_request(url, target_url):
    try:
        async with aiohttp.ClientSession() as session:
            print(f'Proxifying request of "{url}"')
            async with session.get(url, proxy=target_url, timeout=60) as response:
                raw_response = await response.text(encoding='utf-8')
            return web.Response(
                body=raw_response,
                status=response.status,
                headers={'Content-Type': 'text/html', 'Referer': target_url},
            )
    except Exception as err:
        return web.Response(
            text=f'Occurred error while requesting specified address: "{url}"\n'
                 f'Error context: {err.__context__}',
            status=400
        )
