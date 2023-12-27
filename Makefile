# Docker build command
docker-build:
	docker-compose build	

docker-lint:
	docker-compose run --rm app sh -c "flake8"

docker-test:
	# docker-compose run --rm app sh -c "python manage.py test"
	# docker-compose run --rm app sh -c "python manage.py shell -i python -c \"import pytest; pytest.main(['app/tests'])\""
	docker-compose run --rm app sh -c "python manage.py shell -i python -c \"import pytest; pytest.main(['core/tests'])\""

# Creates app django project inside the app folder. Only needs to run once.
docker-create-django-project:
	docker-compose run --rm app sh -c "django-admin startproject app ."

docker-create-django-app:
	docker-compose run --rm app sh -c "python manage.py startapp core"

docker-run:
	docker-compose up