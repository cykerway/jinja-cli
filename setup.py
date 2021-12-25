#!/usr/bin/env python3

'''
setuptools-based setup module; see:

-   https://packaging.python.org/guides/distributing-packages-using-setuptools/
-   https://github.com/pypa/sampleproject
'''

from setuptools import find_packages
from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='jinja-cli',
    version='1.2.2',
    url='https://github.com/cykerway/jinja-cli',
    author='Cyker Way',
    author_email='cykerway@example.com',
    packages=find_packages(),
    description='a command line interface to jinja;',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development',
    ],
    keywords='jinja,engine,interface,template',
    package_data={
    },
    data_files=[
        ('share/jinja-cli/example', [
            'data/example/example.ini',
            'data/example/example.j2',
            'data/example/example.json',
            'data/example/example.xml',
            'data/example/example.yaml',
        ]),
    ],
    install_requires=[
        'Jinja2>=2.11.0',
        'PyYAML',
        'argparse-ext',
        'xmltodict',
    ],
    extras_require={
    },
    entry_points={
        'console_scripts': [
            'jinja=jinja_cli.__main__:main',
        ],
    },
    project_urls={
        'Funding': 'https://paypal.me/cykerway',
        'Source':  'https://github.com/cykerway/jinja-cli',
        'Tracker': 'https://github.com/cykerway/jinja-cli/issues',
    },
)

