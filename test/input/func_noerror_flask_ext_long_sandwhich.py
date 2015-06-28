'''Ensure that pylint finds the exported methods from flask.ext.'''

from flask.ext.admin.model import InlineFormAdmin

MYFORM = InlineFormAdmin
