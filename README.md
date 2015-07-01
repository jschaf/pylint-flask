pylint-flask
===============

[![Build Status](https://travis-ci.org/jschaf/pylint-flask.svg?branch=master)](https://travis-ci.org/jschaf/pylint-flask) [![Coverage Status](https://coveralls.io/repos/jschaf/pylint-flask/badge.svg?branch=master)](https://coveralls.io/r/jschaf/pylint-flask?branch=master) [![PyPI](https://img.shields.io/pypi/v/pylint-flask.svg)](https://pypi.python.org/pypi/pylint-flask) [![License](https://img.shields.io/badge/license-GPLv2%20License-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)

## About

`pylint-flask` is [Pylint](http://pylint.org) plugin for improving code
analysis when editing code using [Flask](http://flask.pocoo.org/).
Inspired by [pylint-django](https://github.com/landscapeio/pylint-django).

### Problems pylint-flask solves:

1. Recognize `flask.ext.*` style imports.  Say you have the following code:

   ```python
    from flask.ext import wtf
    from flask.ext.wtf import validators

    class PostForm(wtf.Form):
        content = wtf.TextAreaField('Content', validators=[validators.Required()])
   ```

   Normally, pylint will throw errors like:

   ```
    E:  1,0: No name 'wtf' in module 'flask.ext'
    E:  2,0: No name 'wtf' in module 'flask.ext'
    F:  2,0: Unable to import 'flask.ext.wtf'
   ```

   As pylint builds it's own abstract syntax tree, `pylint-flask` will translate
   the `flask.ext` imports into the actual module name, so pylint can continue
   checking your code.
   

## Usage

Ensure `pylint-flask` is installed and on your path, and then run pylint using
pylint-flask as a plugin.

```
pip install pylint-flask
pylint --load-plugins pylint_flask [..your module..]
```

## Contributing

Pull requests are always welcome.  Here's an outline of the steps you need to
prepare your code.

1. git clone https://github.com/jschaf/pylint-flask.git
2. cd pylint-flask
3. mkvirtualenv pylint-flask
4. pip install -r dev-requirements.txt
5. git checkout -b MY-NEW-FIX
6. Hack away
7. Make sure everything is green by running `tox`
7. git push origin MY-NEW-FIX
8. Create a pull request

## License

pylint-flask is available under the GPLv2 license.