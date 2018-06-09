import os

from lark import Lark

with open(os.path.join(os.path.dirname(__file__), 'grammar.g'), 'r') as h:
    grammar = h.read()

parser = Lark(grammar, start='specification')


class Specification():
    def __init__(self):
        self.includes = []
        self.modules = []


class Docblock():
    def __init__(self):
        self.docblock = None


class Include(Docblock):
    def __init__(self):
        super().__init__()
        self.identifier = None


class Module(Docblock):
    def __init__(self):
        super().__init__()
        self.name = None


def parse_message_string(pkg_name, msg_name, message_string):
    print('parse_message_string', pkg_name, msg_name)
    global parser
    tree = parser.parse(message_string)

    specification = Specification()
    visit_specification(tree, specification)
    from pprint import pprint
    pprint(specification.__dict__)

    # from lark.tree import pydot__tree_to_png
    # pydot__tree_to_png(tree, '/tmp/%s-%s.png' % (pkg_name, msg_name))


def visit_specification(tree, specification):
    assert tree.data == 'specification'
    for c in tree.children:
        assert c.data == 'definition'
        assert len(c.children) == 1
        c = c.children[0]
        if c.data == 'include_directive':
            include = Include()
            specification.includes.append(include)
            visit_include(c, include)
            continue
        if c.data == 'module_dcl':
            module = Module()
            specification.modules.append(module)
            visit_module(c, module)
            continue


def visit_include(tree, include):
    assert tree.data == 'include_directive'
    assert len(tree.children) == 1
    c = tree.children[0]
    assert c.data in ('h_char_sequence', 'q_char_sequence')
    assert len(c.children) == 1
    c = c.children[0]
    print('include', c.value)
    include.name = c.value


def visit_module(tree, module):
    assert tree.data == 'module_dcl'
    print('module', tree, type(tree), tree.__dict__)
    assert len(tree.children) >= 1
    c = tree.children[0]
    assert c.type == 'IDENTIFIER'
    print(' ', c.value)
    module.name = c.value
    for c in tree.children[1:]:
        assert c.data == 'definition'
        if c.data == 'type_dcl':
            include = Include()
            specification.includes.append(include)
            visit_include(c, include)
            continue
        if c.data == 'const_dcl':
            module = Module()
            specification.modules.append(module)
            visit_module(c, module)
            continue
