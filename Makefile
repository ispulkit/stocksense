.PHONY: clean virtualenv test docker dist dist-upload

clean:
	find . -name '*.py[co]' -delete

virtualenv:
	virtualenv --python=$(which python3) --prompt '|> stocksense <| ' env
	source env/bin/activate
	python --version
	pip install -r requirements-dev.txt
	python setup.py develop
	@echo
	@echo "VirtualENV Setup Complete."
	@echo

test:
	python -m pytest \
		-v \
		--cov=stocksense \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/

docker: clean
	docker build -t stocksense:latest .

dist: clean
	rm -rf dist/*
	python setup.py sdist
	python setup.py bdist_wheel

dist-upload:
	twine upload dist/*
