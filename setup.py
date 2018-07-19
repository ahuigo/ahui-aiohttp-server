from setuptools import setup, find_packages
import os,re
version = "0.1.11"

with open("README.md", "r") as fh:
    long_description = fh.read()

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
    description = "Simple aiohttp Server for both static and python/php file",
    long_description= long_description,
    long_description_content_type="text/markdown",
    author = "ahuigo",
    author_email = "nobody@qq.com",
    license = "MIT",
    url = "http://github.com/ahuigo/ahui-aiohttp-server",   
)

