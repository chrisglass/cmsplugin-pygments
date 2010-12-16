import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cmsplugin-pygments",
    version = "0.7.2",
    url = 'http://github.com/fivethreeo/cmsplugin-pygments',
    license = 'BSD',
    description = "django-cms plugin for pygments",
    author = 'Oyvind Saltvik',
    author_email = 'oyvind.saltvik@gmail.com',
    packages = find_packages(),
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
    zip_safe = False
)
