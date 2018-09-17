build:
	pip install Quik
	pip install PTable
	pip install mock

test:
	python -m unittest discover -b
