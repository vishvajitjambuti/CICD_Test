install:
	pip install --upgrade pip &&\
		pip install -r requirement.txt

test:
	python -m pytest -vv test/test_kidswithCandies.py


format:
	black *.py

lint:


all:

