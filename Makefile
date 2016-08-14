SHELL = /bin/bash

PYTHON ?= /usr/bin/env python2.7
VIRTUALENV_PATH = ./venv


default:
	echo "This is a Makefile of 'Kilometer Python' project"

# Setup virtual environment:
venv:
	virtualenv --python=python2.7 ./venv
	source ./venv/bin/activate
	pip install -r ./requirements.txt
	deactivate

build:
	python setup.py sdist

publish:
	python setup.py register
	python setup.py sdist upload
	# python setup.py bdist_wheel --universal upload
	rm -fr build dist .egg requests.egg-info

# This target is expected to be run by Vagrant provisioning script on `vagrant up`
# "./bin/provision-sandbox.sh"
#sandbox:
#	$(SHELL) ./bin/provision-sandbox.sh

integration-test: build install-test-suite-venv
	$(SHELL) ./test-suite/bin/run-integration-test.sh

#########################################################
# Services management targets
#########################################################

SCRIPTS_PATH = ./provision/scripts

# Accounts Service related targets
run-accounts-service:
	$(SHELL) $(SCRIPTS_PATH)/run-accounts-service.sh
