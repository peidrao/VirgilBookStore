run:
	python manage.py runserver 127.0.0.1:8001

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

commands:
	python manage.py create_genre