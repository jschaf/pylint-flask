# -*- coding: utf-8 -*-
from distutils.core import setup
import sys


_version = '0.6'
_packages = ['pylint_flask']

_short_description = "pylint-flask is a Pylint plugin to aid Pylint in \
recognizing and understanding errors caused when using Flask"


_classifiers = (
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Operating System :: Unix',
    'Topic :: Software Development :: Quality Assurance',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5'
)


_install_requires = [
    'pylint-plugin-utils>=0.2.1'
]


if sys.version_info < (2, 7):
    # pylint 1.4 dropped support for Python 2.6
    _install_requires += [
        'pylint>=1.0,<1.4',
        'astroid>=1.0,<1.3.0',
    ]
else:
    _install_requires += [
        'pylint>=1.0',
        'astroid>=1.0',
    ]

setup(
    name='pylint-flask',
    url='https://github.com/jschaf/pylint-flask',
    author='Joe Schafer',
    author_email='joe@jschaf.com',
    description=_short_description,
    version=_version,
    packages=_packages,
    install_requires=_install_requires,
    license='GPLv2',
    download_url=("https://github.com/jschaf/pylint-flask/tarball/v" +
                  str(_version)),
    classifiers=_classifiers,
    keywords='pylint flask plugin'
)
