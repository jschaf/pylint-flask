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


def flask_transform(_):
    '''Replace Flask module with the imports it lazily loads.'''
    pass
    # module = AstroidBuilder().string_build(code)
    # module.name = 'flask'
    # return module


def is_flask_module(node):
    '''Predicate for checking if we have the flask module.'''
    return node.name == 'flask'

MANAGER.register_transform(nodes.Module,
                           flask_transform,
                           is_flask_module)
