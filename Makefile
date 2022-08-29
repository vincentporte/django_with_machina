PROJECT_PACKAGE := main
PROJECT_CONFIGURATION_PACKAGE := community
DJANGO_SETTINGS_MODULE := $(PROJECT_CONFIGURATION_PACKAGE).settings.dev


init:
	poetry install


.PHONY: c console migrate migrations s server superuser dumpfixtures rebuild_index


# DEVELOPMENT
# ~~~~~~~~~~~
# The following rules can be used during development in order to launch development server, generate
# locales, etc.
# --------------------------------------------------------------------------------------------------

c: console
console:
	poetry run python manage.py shell --settings=$(DJANGO_SETTINGS_MODULE)

migrate:
	poetry run python manage.py migrate --settings=$(DJANGO_SETTINGS_MODULE)

migrations:
	poetry run python manage.py makemigrations --settings=$(DJANGO_SETTINGS_MODULE)

s: server
server:
	poetry run python manage.py runserver 127.0.0.1:8000 --settings=$(DJANGO_SETTINGS_MODULE)

superuser:
	poetry run python manage.py createsuperuser --settings=$(DJANGO_SETTINGS_MODULE)

export_fixtures:
	./scripts/export_fixtures.sh

populate_db:
	poetry run python manage.py loaddata $(PROJECT_CONFIGURATION_PACKAGE)/fixtures/*

rebuild_index:
	poetry run python manage.py rebuild_index
# poetry run python manage.py dumpdata forum_permission --indent 2 --format json --settings=$(DJANGO_SETTINGS_MODULE)

# QUALITY ASSURANCE
# ~~~~~~~~~~~~~~~~~
# The following rules can be used to check code quality, import sorting, etc.
# --------------------------------------------------------------------------------------------------

.PHONY: qa pylint djhtml black flake8
## Trigger all quality assurance checks.
qa:
	poetry run black --check main
	poetry run isort --check main
	poetry run djhtml --check $(shell find main/templates -name "*.html")
	poetry run flake8 main --count --show-source --statistics

pylint:
	poetry run pylint main

black:
	poetry run black main

flake8:
	poetry run flake8 main

isort:
	poetry run isort main

djhtml:
	poetry run djhtml -i $(shell find main/templates -name "*.html")

# TESTING
# ~~~~~~~
# The following rules can be used to trigger tests execution and produce coverage reports.
# --------------------------------------------------------------------------------------------------

.PHONY: t tests
## Alias of "tests".
t: tests
## Run the Python test suite.
tests:
	poetry run py.test

.PHONY: coverage
## Collects code coverage data.
coverage:
	poetry run py.test --cov-report term-missing --cov $(PROJECT_PACKAGE)

.PHONY: spec
## Run the tests in "spec" mode.
spec:
	poetry run py.test --spec -p no:sugar