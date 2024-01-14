run:
	python manage.py runserver

shell:
	python manage.py shell

makemessages:
	django-admin makemessages --all --ignore venv

compilemessages:
	python manage.py compilemessages --ignore venv

migrate:
	python manage.py migrate

make:
	python manage.py makemigrations

test:
	python manage.py test --keepdb

pre-commit:
	pre-commit run --all-files

commands:
	python manage.py create_genre && python manage.py create_authors && python manage.py create_books

