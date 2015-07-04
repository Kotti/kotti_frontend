# Makefile inspired from https://github.com/davidemoro/kotti_project/blob/master/Makefile
#

# You can set these variables from the command line.
VIRTUALENV_NAME = python-dev

.PHONY: help install-prerequisites install run python clean update-requirements

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  install-prerequisites    to install prerequisites"
	@echo "  install                  to build and install a kotti_frontend"
	@echo "  run                      to run kotti_frontend"
	@echo "  python                   to make a python virtualenv environment"
	@echo "  clean-python             to clean python virtualenv"
	@echo "  update-requirements      to make requirements.txt"

install-prerequisites:
	@echo ">>> Install prerequisites"
	sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
	sudo apt-get install build-essential python python-dev python-virtualenv
	@echo ">>> End prerequisites"

install:
	@echo ">>> Install production"
	make clean-python
	make python
	make update-requirements
	$(VIRTUALENV_NAME)/bin/pip install -r requirements.txt
	@echo ">>> End install production"

run:
	$(VIRTUALENV_NAME)/bin/pserve development.ini --reload

python:
	@echo ">>> Create virtualenv"
	virtualenv --no-site-packages $(VIRTUALENV_NAME)
	$(VIRTUALENV_NAME)/bin/pip install --upgrade pip

clean-python:
	@echo ">>> Clear virtualenv production"
	rm -rf $(VIRTUALENV_NAME)

update-requirements:
	@echo ">>> Update requirements.txt"
	$(VIRTUALENV_NAME)/bin/pip install -r template-requirements.txt
	$(VIRTUALENV_NAME)/bin/pip freeze -r template-requirements.txt | sed '1,2d' > requirements.txt
