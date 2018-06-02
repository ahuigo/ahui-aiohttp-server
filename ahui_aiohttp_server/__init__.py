import sys,os,io,json, time
from pathlib import Path
from contextlib import redirect_stdout
import asyncio 
from aiohttp import web
import logging; 
logging.basicConfig(level=logging.INFO)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-ho", "--host", default='127.0.0.1', )
parser.add_argument("-p", "--port", type=int,default=5000)
args = parser.parse_args()

'''
wsgi application
'''
def index(request):
    print(request.match_info)
    path = request.path[1:]
    if '..' in path:
        return web.Response(status=500, body='Insecured path')
    if not os.path.exists(path):
        return web.Response(status=404, body=f'not path:{path}'.encode())
    if path.endswith('.py'):
        logging.info('Excute python:'+path)
        f = io.StringIO()
        with redirect_stdout(f):
            code = open(path).read()
            exec(code)
            _locals=locals()
            if 'aiohttp_app' in _locals:
                return _locals['aiohttp_app'](request)
            elif 'echo_app' in locals():
                _locals['echo_app'](request)
        out = f.getvalue()
        return web.Response(body=out.encode())
    else:
        return web.FileResponse(f'./{path}')

'''
wsgi server
'''
async def init(loop):
    port = args.port
    host = args.host
    app = web.Application(loop=loop)
    app.router.add_route('*', '/{tail:.*}', index)
    srv = await loop.create_server(app.make_handler(), host, port)
    logging.info(f'start server: {host}:{port} ')
    logging.info('current work dir:'+os.getcwd())
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


