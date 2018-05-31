from setuptools import setup, find_packages
import re
version = "0.0.5"
s = open('setup.py').read()
s = re.sub(r'(?<=\n)(version *= *")(\d+\.\d+\.)(\d+)"', 
    lambda m: 'version = "%s%d"' % (m.group(2), int(m.group(3))+1),
    s,1)
open('setup.py', 'w').write(s)

setup(
    name='pyhttp-server',
    version = version,
    install_requires=[ 'flask>=0.12', ],
    package_dir={"":"."},
    entry_points = {
        #'console_scripts': ['pyhttp_server=pyhttp_server:main', ],
    },
    py_modules=['pyhttp_server'],

    author = "ahuigo",
    author_email = "nobody@qq.com",
    description = "Http Server for both static and python file",
    license = "GPL",
    url = "http://github.com/ahuigo/pyhttp-server",   
)
