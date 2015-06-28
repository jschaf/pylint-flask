'''pylint_flask module'''

from astroid import MANAGER
from astroid.builder import AstroidBuilder
from astroid import nodes
import textwrap


def register(_):
    '''register is expected by pylint for plugins, but we are creating a transform,
     not registering a checker.

    '''
    pass


def flask_transform(node):
    '''Replace Flask module with the imports it lazily loads.'''
    new_node = nodes.Import()
    new_node.names = [('flask_wtf', 'wtf')]
    new_node.lineno = node.lineno
    new_node.fromlineno = node.fromlineno
    new_node.tolineno = node.tolineno
    new_node.col_offset = node.col_offset
    new_node.parent = node.parent

    return new_node

def flask_transform_long_mod_name():
    pass
    # from flask.ext.wtf import Form
    # from flask_wtf import Form

def is_flask_module(node):
    '''Predicate for checking if we have the flask module.'''
    return node.modname == 'flask.ext'

MANAGER.register_transform(nodes.From,
                           flask_transform,
                           is_flask_module)
