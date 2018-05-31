from flask import Flask, request, send_from_directory
import sys,os,io
from pathlib import Path
from contextlib import redirect_stdout
app = Flask(__name__, )

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def catch_all(path):
    print('catch_all: '+path)
    print(os.path.exists(path))
    if not os.path.exists(path):
        return 'no paht:'+path, 404
    path = Path(path)
    if path.name.endswith('.py'):
        print('handle py')
        f = io.StringIO()
        with redirect_stdout(f):
            print(os.getcwd())
            path = Path(path)
            os.environ['SCRIPT_FILENAME']='a.py'
            code = open(path).read()
            exec(code)
        out = f.getvalue()
        return out
    return send_from_directory('.', path)

def main():
    app.run()

if __name__ == '__main__':
    app.run()