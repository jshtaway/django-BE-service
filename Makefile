# Docker build command
docker-build:
	docker-compose build	

docker-test:
	docker-compose run --rm app sh -c "flake8"
	docker-compose run --rm app sh -c "python manage.py test"
	docker-compose run --rm app sh -c "python -m pytest app/tests"

docker-create-django:
	docker-compose run --rm app sh -c "django-admin startproject app ."

docker-run:
	docker-compose up