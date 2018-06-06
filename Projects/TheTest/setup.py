try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Test project',
    'author': 'Mitterdini the Great',
    'url': 'github?',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['TheTest'],
    'scripts': ['bin/runnit'],
    'name': 'TheTest'
}

setup(**config)
