# qc - query code

The idea is to provide ways to query code (so far, just C code). It'll be possible
to query for functions that calls some function, functions called by some function
and others kinds of queries.

## Use

Basic example:

```python
from qc.parser import analyze
data = analyze("tests/test_file1.c")

[func.name for func in data.functions if func.it_calls("read")]
```

Get max if nest level:

```python
from qc.parser import parse
code = """
    int main (int argc, char *argv[]) {
        char *space;
        space = malloc(sizeof(char) * 10);
        if (space == NULL) {
            if (1 > 2) {
                if (3 == 4) {
                    return -1;
                }
            } else {
                if (1 == 1) {
                    return -1;
                } else {
                    if (1 == 2) {
                        return -1;
                    } else {
                        if (1 == 2) {
                            return -1;
                        } else {
                            return -1;
                        }
                    }
                }
            }
            return -1;
        }
        return 0;
    }
"""

parsed_content = parse(code, "<string>")
main = parsed_content.functions[0]
assert 5 == main.if_nest_level()
```

## Testing

```sh
make test
```

## Coverage

```sh
make coverage
```

## Contact

felipecruz@loogica.net
