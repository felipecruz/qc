test:
	py.test --verbose .

coverage:
	py.test --cov-report html --cov .

clean:
	rm -rf htmlcov/
	find . -name __pycache__ -prune | xargs rm -rf
