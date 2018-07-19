# Ahui-aiohttp-server
This is a simple http async server which extends `python -m http.server`.\
(WARN: It's recommended for development and testing and not for production environments):
- Support print to http response directly (same as php's echo)
- Support async-await
- Support php, python

## Install

    pip install ahui-aiohttp-server
    pip3 install ahui-aiohttp-server

## Start server

    $ tree .
    ./
        app/
            echo1.py
            echo2.py
            echo.php
            return.py
        js/
            test.js
    $ python -m ahui_aiohttp_server
    $ python -m ahui_aiohttp_server --host 127.0.0.1 --port 5000

## Access server

### Access via echo server(php-like):

    $ cat app/echo1.py
    print('Hello World!')

    $ curl http://127.0.0.1:5000/app/echo1.py
    Hello World!
    $ curl http://127.0.0.1:5000/js/test.js
    <js content>
    $ curl http://127.0.0.1:5000/app/echo.php
    <js content>

If you want to get request data(such as: `get, post, cookie, ...`, use `aiohttp_handler(request)` instead:

    $ cat app/echo2.py
    def aiohttp_handler(request):
        print(request.query)    # use print 

    $ curl http://127.0.0.1:5000/app/echo2.py?var=value
    {'var':'value'}

### Access via normal aiohttp server:

    $ cat app/return.py
    from aiohttp import web
    async def aiohttp_handler(request):
        data = await request.post()
        return web.Response(body=str(data)) # use return

    $ curl http://127.0.0.1:5000/app/return.py?var=value - 'k1=v2'
    {'k1':'v2'}

### Access static file:

    $ curl http://127.0.0.1:5000/js/test.js
    <js content>

## Required
1. aiohttp
2. python>=3.6
