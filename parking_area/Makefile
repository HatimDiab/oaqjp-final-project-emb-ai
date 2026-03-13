.PHONY: compile install install-tools lint run

install-tools:
	python3.11 -m pip install pip-tools

compile: install-tools
	python3.11 -m pip freeze > requirements.ref 
	pip-compile requirements.in -o requirements.txt --constraint requirements.ref

install: compile
	python3.11 -m pip install -r requirements.txt

lint:
	pylint server.py

run:
	python3.11 server.py