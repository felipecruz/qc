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
