from aiohttp import web

cors_headers = {
    'Allow': '*',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': '*',
    'Access-Control-Allow-Methods': '*',
    'Access-Control-Allow-Credentials': 'true',
}


@web.middleware
async def cors_middleware(request, handler) -> web.Response:
    """AIOHTTP Middleware to set CORS headers"""
    try:
        response: web.Response = await handler(request)
        if response.headers:
            response.headers.update(cors_headers)
        return response

    except web.HTTPException as e:
        return web.json_response(
            {'error': e.reason}, headers=cors_headers, status=e.status
        )

    except Exception as e:
        print(
            'Occurred unhandled error while processing request: '
            f'{e.__context__ if e.__context__ is not None else e}'
        )
        raise e
