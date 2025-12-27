run:
	python3 manage.py runserver

shell:
	python3 manage.py shell

populate:
	python3 manage.py 0_create_superuser
	python3 manage.py 1_create_genre
	python3 manage.py 2_create_authors
	python3 manage.py 3_create_books

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
