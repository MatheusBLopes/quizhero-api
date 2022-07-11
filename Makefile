PROJECT_NAME = $(shell pwd | rev | cut -f1 -d'/' - | rev)

runserver:
	poetry run python quizhero-api/manage.py runserver

build-image:
	docker build -t registry.heroku.com/quizhero/web .

push-image:
	docker push registry.heroku.com/quizhero/web

release:
	heroku container:release -a quizhero web

delete-last-image:
	docker rmi registry.heroku.com/quizhero/web

deploy:
	@make build-image
	@make push-image
	@make release

lint:
	poetry run pre-commit run --all-files

logs:
	heroku logs --tail -a quizhero

run-gunicorn:
	gunicorn -c gunicorn_config.py quizhero_api.wsgi:application
