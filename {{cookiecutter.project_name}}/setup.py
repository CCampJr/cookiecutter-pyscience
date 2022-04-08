#! /usr/bin/env python
"""Setup for {{cookiecutter.project_name}}."""

import codecs
import os

from setuptools import find_packages, setup

# get __version__ from _version.py
ver_file = os.path.join('{{cookiecutter.project_name}}', '_version.py')
with open(ver_file) as f:
    exec(f.read())

DISTNAME = '{{cookiecutter.project_name}}'
DESCRIPTION = '{{cookiecutter.short_description}}'
with codecs.open('README.rst', encoding='utf-8-sig') as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = '{{cookiecutter.creator_name}}'
MAINTAINER_EMAIL = '{{cookiecutter.creator_email}}'
URL = ''
LICENSE = 'Public Domain'
DOWNLOAD_URL = ''
VERSION = __version__  # noqa: F821
with open('./requirements.txt','r') as f:
    INSTALL_REQUIRES = f.read().splitlines()
CLASSIFIERS = ['Development Status :: 3 - Alpha',
               'Intended Audience :: Science/Research',
               'Intended Audience :: Developers',
               'Programming Language :: Python',
               'Topic :: Software Development',
               'Topic :: Scientific/Engineering',
               'Operating System :: Microsoft :: Windows',
               'Operating System :: POSIX',
               'Operating System :: Unix',
               'Operating System :: MacOS',
               'Programming Language :: Python :: 3 :: Only',
               'Topic :: Scientific/Engineering :: Information Analysis',
               'Topic :: Scientific/Engineering :: Mathematics',
               'Topic :: Scientific/Engineering :: Physics']
EXTRAS_REQUIRE = {
    'tests': [
        'pytest',
        'pytest-cov'],
    'docs': [
        'sphinx',
        'sphinx-gallery',
        'sphinx_rtd_theme',
        'numpydoc'
    ]
}

setup(name=DISTNAME,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      description=DESCRIPTION,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      long_description=LONG_DESCRIPTION,
      zip_safe=False,  # the package can run out of an .egg file
      classifiers=CLASSIFIERS,
      packages=find_packages(),
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE)
