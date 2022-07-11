PROJECT_NAME = $(shell pwd | rev | cut -f1 -d'/' - | rev)

runserver:
	poetry run python quizhero-api/manage.py runserver

build-image:
	docker build -t $(PROJECT_NAME) .

lint:
	poetry run pre-commit run --all-files
