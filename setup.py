try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION="0.1.0"

config = {
    'description': 'pydnx',
    'author': 'Sean Mosely',
    'url': 'URL to get at it',
    'download_url': 'Where to download it',
    'author_email': 'sean.mosely@gmail.com',
    'version': VERSION,
    'install_requires': ['lxml==3.6.4',],
    'packages': ['pydnx'],
    'scripts': [],
    'name': 'pydnx',
    'download_url': 'https://github.com/NLNZDigitalPreservation/pydnx/archive/v'+VERSION+'.tar.gz',
    'license': 'MIT',
}

setup(**config)
