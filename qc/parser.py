from __future__ import print_function
import sys

from pycparser.c_parser import CParser
from pycparser.c_generator import CGenerator
from pycparser.c_ast import NodeVisitor
from pycparser import c_ast

from domain import Function

class ASTVisitor(NodeVisitor):
    def __init__(self):
        self.current_parent = None
        self.functions = []

    def generic_visit(self, node):
        if isinstance(node, c_ast.FuncDef):
            func = Function(node, node.decl.name, None, node.body.block_items)
            self.functions.append(func)

        oldparent = self.current_parent
        self.current_parent = node

        for c_name, child in node.children():
            self.visit(child)

        self.current_parent = oldparent

def remove_includes(file_lines):
    no_include_lines = []
    for line in file_lines:
        if line.startswith("#include"):
            continue
        no_include_lines.append(line)
    return no_include_lines

def analyze(file_path):
    file_content, file_name = get_file_content(file_path)
    return parse(file_content, file_name)

def parse(file_content, file_name):
    parser = CParser()
    generator = CGenerator()

    ast = parser.parse(file_content, file_name, debuglevel=0)

    test_finder = ASTVisitor()
    test_finder.visit(ast)

    return test_finder

def get_file_content(file_path):
    file_name = file_path.split('/')[-1:][0]
    file_pwd = "/".join(file_path.split('/')[:-1])

    lines = remove_includes(open(file_path, "rt").readlines())
    file_content = "\n".join(lines)
    return file_content, file_name
