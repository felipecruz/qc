import pytest

from qc.parser import parse, remove_includes, analyze

def test_analyze():
    parsed_content = analyze("tests/test_file1.c")
    assert parsed_content

def test_remove_includes():
    content = ['#include <stdio.h>', 'include "test.h"', '#include "t.h"']
    data = remove_includes(content)

    assert 1 == len(data)
    assert 'include "test.h"' == data[0]

def test_parse():
    parsed_content = parse("int main (int argc, char *argv[]) { return 0; }",
                           "<string>")
    assert parsed_content

def test_parse_check_functions():
    parsed_content = parse("int main (int argc, char *argv[]) { return 0; }",
                           "<string>")
    assert parsed_content
    assert 1 == len(parsed_content.functions)
    assert "main" == parsed_content.functions[0].name

def test_parse_check_functions_calling_malloc():
    code = """
        int main (int argc, char *argv[]) {
            char *space;
            space = malloc(sizeof(char) * 10);
            if (space == NULL) {
                return -1;
            }
            return 0;
        }
    """
    parsed_content = parse(code, "<string>")
    assert parsed_content
    assert 1 == len(parsed_content.functions)
    assert "main" == parsed_content.functions[0].name
    assert "main" == [function.name for function
                                    in parsed_content.functions
                                    if function.it_calls("mallor")][0]
