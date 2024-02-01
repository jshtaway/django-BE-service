# Docker build command
docker-build:
	docker-compose build	

docker-lint:
	docker-compose run --rm app sh -c "flake8"

docker-test:
	# docker-compose run --rm app sh -c "python manage.py test"
	# docker-compose run --rm app sh -c "python manage.py shell -i python -c \"import pytest; pytest.main(['-s', 'app/tests'])\""
	docker-compose run --rm app sh -c "python manage.py shell -i python -c \"import pytest; pytest.main(['-s', 'core/tests'])\""

# Creates app django project inside the app folder. Only needs to run once.
docker-create-django-project:
	docker-compose run --rm app sh -c "django-admin startproject app ."

docker-create-django-app:
	docker-compose run --rm app sh -c "python manage.py startapp core"

docker-run:
	docker-compose up

docker-stop:
	docker-compose down

docker-makemigrations:
	docker-compose run --rm app sh -c "python manage.py makemigrations"

# apply migrations to the project
docker-migrate:
	docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"