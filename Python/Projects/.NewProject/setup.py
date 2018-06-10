try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'This makes a new project template',
    'author': 'Mittedini the Great',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NewProject'],
    'scripts': ['bin/new_project'],
    'name': 'New_Project'
}

setup(**config)
