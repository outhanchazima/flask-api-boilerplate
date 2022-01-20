.ONESHELL:

.PHONY: clean install run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt;

# tests:
# 	. venv/bin/activate; \
# 	python manage.py test

run:
	. venv/bin/activate; \
	python manage.py run

all: clean install tests run
