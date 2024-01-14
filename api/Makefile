run:
	python3 manage.py runserver

shell:
	python3 manage.py shell

makemessages:
	django-admin makemessages --all --ignore venv

compilemessages:
	python3 manage.py compilemessages --ignore venv

migrate:
	python3 manage.py migrate

make:
	python3 manage.py makemigrations

test:
	python3 manage.py test --keepdb

fmt:
	ruff check . --fix
	ruff format .

pre-commit:
	pre-commit run --all-files

commands:
	python3 manage.py create_genre && python manage.py create_authors && python manage.py create_books

