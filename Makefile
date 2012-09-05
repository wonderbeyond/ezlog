MANAGE=python manage.py
CACHE_TABLE=ezlog_cache

runserver:
	$(MANAGE) runserver 0.0.0.0:8000
rmpyc: 
	find . -type f -name "*.pyc"|xargs rm -rf
syncdb:
	$(MANAGE) syncdb
	$(MANAGE) migrate blog
	$(MANAGE) migrate plog
	$(MANAGE) createcachetable $(CACHE_TABLE)
