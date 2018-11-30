#!/usr/bin/env python3

'''
setuptools based setup module;

see <https://packaging.python.org/en/latest/distributing.html>;
'''

from os import path
from setuptools import find_packages
from setuptools import setup

here = path.abspath(path.dirname(__file__))

##  get long description from readme file;
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    ##  ========================================================================
    ##  required for pypi upload;
    ##  ========================================================================

    ##  project name;
    ##
    ##  this determines how users install this project:
    ##
    ##      pip install sampleproject
    ##
    ##  and where this project lives on pypi:
    ##
    ##  <https://pypi.org/project/sampleproject/>
    ##
    ##  this name is registered for you the first time you publish this package;
    ##
    ##  name specification:
    ##
    ##  <https://packaging.python.org/specifications/core-metadata/#name>
    ##
    name='jinja-cli',

    ##  project version;
    ##
    ##  version specification (pep 440):
    ##
    ##  <https://www.python.org/dev/peps/pep-0440/>;
    ##
    ##  single-sourcing techniques:
    ##
    ##  <https://packaging.python.org/en/latest/single_source_version.html>
    ##
    version='1.1.2',

    ##  project homepage;
    ##
    ##  this arg corresponds to "home-page" metadata field:
    ##
    ##  <https://packaging.python.org/specifications/core-metadata/#home-page-optional>
    ##
    url='https://github.com/cykerway/jinja-cli',

    ##  author name;
    author='Cyker Way',

    ##  author email address;
    author_email='cykerway@example.com',

    ##  packages;
    ##
    ##  you can provide a list of packages manually or use `find_packages()`;
    ##
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    ##  ========================================================================
    ##  optional for pypi upload;
    ##  ========================================================================

    ##  a one-line description;
    ##
    ##  this arg corresponds to "summary" metadata field:
    ##
    ##  <https://packaging.python.org/specifications/core-metadata/#summary>
    ##
    description='a command line interface to jinja;',

    ##  a longer description shown on project homepage on pypi;
    ##
    ##  this is often the same as the readme;
    ##
    ##  this arg corresponds to "description" metadata field:
    ##
    ##  <https://packaging.python.org/specifications/core-metadata/#description-optional>
    ##
    long_description=long_description,

    ##  longer description content type;
    ##
    ##  valid values are: `text/plain`, `text/x-rst`, `text/markdown`;
    ##
    ##  this arg corresponds to "description-content-type" metadata field:
    ##
    ##  <https://packaging.python.org/specifications/core-metadata/#description-content-type-optional>
    ##
    long_description_content_type='text/markdown',

    ##  classifiers categorizing this project;
    ##
    ##  see <https://pypi.org/classifiers/>;
    ##
    classifiers=[
        ##  development status;
#        'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
#        'Development Status :: 5 - Production/Stable',

        ##  intended audience;
        'Intended Audience :: Developers',
#        'Intended Audience :: End Users/Desktop',

        ##  topic;
#        'Topic :: Desktop Environment',
#        'Topic :: Games/Entertainment',
#        'Topic :: Multimedia',
#        'Topic :: Office/Business',
#        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
#        'Topic :: System',

        ##  license;
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
#        'License :: OSI Approved :: BSD License',
#        'License :: OSI Approved :: MIT License',

        ##  supported python versions;
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    ##  project keywords;
    ##
    ##  these keywords will appear on the project page;
    ##
    keywords='jinja template engine',

    ##  package data;
    ##
    ##  this is a dict mapping package names to a list of relative path names
    ##  (or glob patterns) that should be copied into the package when
    ##  installed; the path names are interpreted relative to the package dir;
    ##
    package_data={
#        'sample': ['*.bin'],
    },

    ##  additional data files;
    ##
    ##  this is a sequence of `(dir, files)` pairs; each `(dir, files)` pair
    ##  specifies the install dir and the files to install there; if `dir` is a
    ##  relative path, it is relative to the install prefix (`sys.prefix` or
    ##  `sys.exec_prefix`); each file in `files` is interpreted relative to the
    ##  `setup.py` script;
    ##
    ##  see <https://docs.python.org/3/distutils/setupscript.html#installing-additional-files>;
    ##
    data_files=[
        ('share/jinja-cli/example', [
            'data/example/example.ini',
            'data/example/example.j2',
            'data/example/example.json',
            'data/example/example.xml',
            'data/example/example.yaml',
        ]),
    ],

    ##  package dependencies;
    ##
    ##  this is a list of packages that this project depends on; these packages
    ##  will be installed by pip when this project is installed;
    ##
    install_requires=[
        'Jinja2',
        'PyYAML',
        'argparse-better',
        'xmltodict',
    ],

    ##  extra package dependencies;
    ##
    ##  this is a dict mapping extras (optional features of this project) to a
    ##  list of packages that those extras depend on;
    ##
    ##  users will be able to install these using the extras syntax:
    ##
    ##      pip install sampleproject[dev]
    ##
    ##  see <https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies>
    ##
    extras_require={
#        'dev': ['check-manifest'],
#        'test': ['coverage'],
    },

    ##  to create executable scripts, use entry points:
    ##
    ##  <https://setuptools.readthedocs.io/en/latest/setuptools.html#automatic-script-creation>
    ##
    ##  for example, the following would provide a console script `sample-cli`
    ##  which executes the `main` function in package `sample.cli`, and a gui
    ##  script `sample-gui` which executes the `main` function in package
    ##  `sample.gui`;
    entry_points={
        'console_scripts': [
            'jinja=jinja_cli.__main__:main',
        ],
#        'gui_scripts': [
#            'sample-gui=sample.gui:main',
#        ],
    },

    ##  additional urls that are relevant to this project;
    ##
    ##  examples include: where the package tracks issues, where the source is
    ##  hosted, where to say thanks to the package maintainers, and where to
    ##  support the project financially; the keys are used to render the link
    ##  texts on pypi;
    ##
    ##  this arg corresponds to "project-url" metadata fields:
    ##
    ##  <https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use>
    ##
    project_urls={
        'Bug Reports': 'https://github.com/cykerway/jinja-cli/issues',
#        'Funding': 'https://donate.pypi.org',
#        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/cykerway/jinja-cli',
    },
)

