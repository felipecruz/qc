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
                             isinstance(call.rvalue, c_ast.FuncCall) and
                             call.rvalue.name.name == inner_function_name)])

    def if_nest_level(self):
        def nest_meter(if_statement):
            values = []
            if hasattr(if_statement, 'iftrue') and if_statement.iftrue and \
               len(if_statement.iftrue.block_items):
                nested_ifs = [if_stm for if_stm
                                     in if_statement.iftrue.block_items
                                     if isinstance(if_stm, c_ast.If)]
                for nested_if in nested_ifs:
                    values.append(1 + nest_meter(nested_if))
            if hasattr(if_statement, 'iffalse') and if_statement.iffalse and \
               len(if_statement.iffalse.block_items):
                nested_ifs = [if_stm for if_stm
                                     in if_statement.iffalse.block_items
                                     if isinstance(if_stm, c_ast.If)]
                for nested_if in nested_ifs:
                    values.append(1 + nest_meter(nested_if))

            if not values:
                return 1

            return max(values)

        values = []
        for block in self.blocks:
            if isinstance(block, c_ast.If):
                values.append(nest_meter(block))

        return max(values)


    def __str__(self):
        return str(self.node)
