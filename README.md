# Ahui-aiohttp-server
This is a simple http async server which extends `python -m http.server`.\
(WARN: It's recommended for development and testing and not for production environments):
- Support print to http response (same as php)
- Support async-await

## Install

    pip install ahui-aiohttp-server
    pip3 install ahui-aiohttp-server

## Usage
### Start server

    $ python -m ahui-aiohttp-server
    $ python -m ahui-aiohttp-server --host 127.0.0.1 --port 5000

### Access server
List files in current dir:

    app/
        echo1.py
        echo2.py
        return.py
    js/
        test.js

#### Access via echo server(php-like):

    $ cat echo1.py
    print('Hello World!')

    $ curl http://127.0.0.1:5000/app/echo1.py
    Hello World!

If you want to get request data(such as: `get, post, cookie, ...`, use `aiohttp_handler(request)` instead:

    $ cat echo2.py
    def aiohttp_handler(request):
        print(request.query)    # use print 

    $ curl http://127.0.0.1:5000/app/echo2.py?var=value
    {'var':'value'}

#### Access via normal aiohttp server:

    $ cat return.py
    from aiohttp import web
    async def aiohttp_handler(request):
        data = await request.post()
        return web.Response(body=str(data)) # use return

    $ curl http://127.0.0.1:5000/app/return.py?var=value - 'k1=v2'
    {'k1':'v2'}

#### Access static file:

    $ curl http://127.0.0.1:5000/js/test.js

## Required
1. aiohttp
2. python>=3.6
