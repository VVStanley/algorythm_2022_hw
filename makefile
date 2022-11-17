test:
	pytest dz*/test*

test_cov:
	pytest --cov=dz* tests

linter:
	flake8 dz*

mypy:
	mypy dz*
