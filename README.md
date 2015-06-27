pylint-flask
===============

[![Build Status](https://travis-ci.org/jschaf/pylint-flask.svg?branch=master)](https://travis-ci.org/jschaf/pylint-flask) [![Coverage Status](https://coveralls.io/repos/jschaf/pylint-flask/badge.svg)](https://coveralls.io/r/jschaf/pylint-flask)

## About

`pylint-flask` is [Pylint](http://pylint.org) plugin for improving code
analysis when editing code using [Flask](http://flask.pocoo.org/).
Inspired by [pylint-django](https://github.com/landscapeio/pylint-django).

## Usage

Ensure `pylint-flask` is installed and on your path, and then run pylint.

```
pip install pylint-flask
pylint --load-plugins pylint_flask [..your module..]
```

## License

pylint-flask is available under the GPLv2 license.