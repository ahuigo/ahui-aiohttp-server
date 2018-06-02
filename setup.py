from setuptools import setup, find_packages
import re
version = "0.0.16"

setup(
    name='ahui_aiohttp_server',
    version = version,
    install_requires=[ 'aiohttp', ],
    packages=['ahui_aiohttp_server'],
    py_modules=['ahui_aiohttp_server'],
    python_requires='>=3.5.3',
    package_dir={"":"."},
    entry_points = {
        #'console_scripts': ['aiohttp_server=pyhttp_server:main', ],
    },

    description = "Aiohttp Server for both static and python file",
    long_description="Aiohttp Server for both static and python file"
    author = "ahuigo",
    author_email = "nobody@qq.com",
    license = "MIT",
    url = "http://github.com/ahuigo/ahui-aiohttp-server",   
)

s = open('setup.py').read()
s = re.sub(r'(?<=\n)(version *= *")(\d+\.\d+\.)(\d+)"', 
    lambda m: 'version = "%s%d"' % (m.group(2), int(m.group(3))+1),
    s,1)
open('setup.py', 'w').write(s)
