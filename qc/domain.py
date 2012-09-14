from pycparser import c_ast

class Function(object):
    def __init__(self, node, name, params, blocks):
        self.node = node
        self.name = name
        self.params = params
        self.blocks = blocks

    def it_calls(self, inner_function_name):
        return any([call for call
                         in self.blocks
                         if (isinstance(call, c_ast.FuncCall) and
                            call.name.name == inner_function_name) or
                            (isinstance(call, c_ast.Assignment) and
                             isinstance(call.rvalue, c_ast.FuncCall))])

    def __str__(self):
        return str(self.node)
