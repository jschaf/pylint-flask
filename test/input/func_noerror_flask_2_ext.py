'''Ensure that pylint finds the exported methods from flask.ext.'''

from flask.ext import wtf, bcrypt

MYFORM = wtf.Form

YOLO = bcrypt.Bcrypt
