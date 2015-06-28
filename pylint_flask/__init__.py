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

def copy_node_info(src, dest):
    """Copy information from src to dest

    Every node in the AST has to have line number information.  Get
    the information from the old stmt."""
    for attr in ['lineno', 'fromlineno', 'tolineno',
                 'col_offset', 'parent']:
        if hasattr(src, attr):
            setattr(dest, attr, getattr(src, attr))

def transform_flask_from_import(node):
    '''Translates a flask.ext from-style import into a regular, non-magical import.

    Translates:
        from flask.ext import wtf, bcrypt as fcrypt
    Into:
        import flask_wtf as wtf, flask_bcrypt as fcrypt

    '''
    new_names = []
    for (name, as_name) in node.names:
        actual_module_name = 'flask_{}'.format(name)
        new_names.append((actual_module_name, as_name or name))

    new_node = nodes.Import()
    copy_node_info(node, new_node)
    new_node.names = new_names
    return new_node

def flask_transform_long_mod_name():
    pass
    # from flask.ext.wtf import Form
    # from flask_wtf import Form

def is_flask_from_import(node):
    '''Predicate for checking if we have the flask module.'''
    return node.modname == 'flask.ext'

MANAGER.register_transform(nodes.From,
                           transform_flask_from_import,
                           is_flask_from_import)
