from urllib.parse import urlparse, ParseResult


def parse_url(raw_url) -> str:
    if 'http' in raw_url or 'https' in raw_url:
        url: ParseResult = urlparse(raw_url)
        proto = url.scheme
        if proto == 'https':
            proto = proto[:-1]
            return f'{proto}://{url.netloc}'

        render_url = url.geturl()
        return render_url
    else:
        url = f'http://{raw_url}'
        return url
