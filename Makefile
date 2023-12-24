# Docker build command
docker-build:
	docker-compose build	

docker-test:
	docker-compose run --rm app sh -c "flake8"
	docker-compose run --rm app sh -c "python manage.py test"
	docker-compose run --rm app sh -c "python manage.py shell -i python -c \"import pytest; pytest.main(['app/tests'])\""

# Creates app django project inside the app folder. Only needs to run once.
docker-create-django:
	docker-compose run --rm app sh -c "django-admin startproject app ."

docker-run:
	docker-compose up