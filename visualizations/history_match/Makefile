all: build


.PHONY: build install
build:
	python setup.py build

dev-install:
	pip install -e .

install: build
	python setup.py install

test:
	py.test --cov=webviz_history_match --cov-fail-under=97 tests/

lint:
	pycodestyle webviz_history_match examples tests
