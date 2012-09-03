MANAGE=python manage.py

runserver:
	$(MANAGE) runserver 0.0.0.0:8000
rmpyc: 
	find . -type f -name "*.pyc"|xargs rm -rf
