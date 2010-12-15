import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cmsplugin-pygments",
    version = "0.7.1",
    url = 'http://github.com/fivethreeo/cmsplugin-pygments',
    license = 'BSD',
    description = "django-cms plugin for pygments",
    author = 'Oyvind Saltvik',
    author_email = 'oyvind.saltvik@gmail.com',
    packages = find_packages('.'),
    package_dir = {'':'.'},
    install_requires=[
        'pygments',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    include_package_data=True,
    package_data={
        'cmsplugin_pygments': [
            'templates/cmsplugin_pygments/*.html',
        ]
    },
    zip_safe = False
)
