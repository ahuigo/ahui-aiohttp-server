import sys
import os
import io
import json
import time
from pathlib import Path
from contextlib import redirect_stdout
import asyncio
from aiohttp import web
import asyncio
import logging
import sys
logging.basicConfig(level=logging.INFO)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-ho", "--host", default='127.0.0.1', )
parser.add_argument("-p", "--port", type=int, default=5000)
parser.add_argument("-d", "--dir", type=str, default='.')
args = parser.parse_args()

'''
wsgi application
'''


async def index(request):
    print(request.match_info)
    #print(await request.post())
    path = request.path[1:]
    if '..' in path:
        return web.Response(status=500, body='Insecured path')
    #if not os.path.exists(path): return web.Response(status=404, body=f'not path:{path}'.encode())
    if path.endswith('.py'):
        logging.info('Execute path:'+path)
        f = io.StringIO()
        with redirect_stdout(f):
            code = open(path).read()
            exec(code)
            _locals = locals()
            res = None
            if 'aiohttp_handler' in _locals:
                logging.info('Execute aiohttp_handler')
                res = _locals['aiohttp_handler'](request)
            if res:
                if asyncio.iscoroutine(res):
                    logging.info('use async coroutine')
                    res = await res
                if isinstance(res, web.Response):
                    logging.info('Get Web.Response')
                    return res
                elif res is not None:
                    logging.info('Get string')
                    return web.Response(body=str(res))
        out = f.getvalue()
        return web.Response(body=out)
    elif path.endswith('.php'):
        from subprocess import check_output
        out = check_output(['php', path])
        return web.Response(body=out)
    else:
        if not os.path.exists(path): #return web.Response(status=404, body=f'not path:{path}'.encode())
            path += '.html'
        ext = os.path.splitext(path)[1][1:]
        headers = {}
        exts = {
                'html': 'text/html',
                'htm': 'text/html',
                'js': 'application/javascript',
                'mjs': 'application/javascript',
                'md': 'text/plain',
            }
        if ext in exts:
            headers = {'Content-Type': exts[ext]}
        else:
            #headers = {'Content-Type': 'text/plain'}
            headers = {}
        print({'heades':headers,'ext':ext,'path':path})
        return web.FileResponse(f'./{path}', headers=headers)

'''
wsgi server
'''


async def init(loop):
    port = args.port
    host = args.host
    os.chdir(args.dir)
    app = web.Application(loop=loop)
    app.router.add_route('*', '/{tail:.*}', index)
    srv = await loop.create_server(app.make_handler(), host, port)
    logging.info(f'start server: {host}:{port} ')
    logging.info('current work dir:'+os.getcwd())
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
