MANAGE=python manage.py
CACHE_TABLE=ezlog_cache

runserver:
	$(MANAGE) runserver 0.0.0.0:8000

rmpyc: 
	find . -type f -name "*.pyc"|xargs rm -rf

syncdb:
	[ -d data ] || mkdir data
	$(MANAGE) syncdb
	$(MANAGE) migrate blog
	$(MANAGE) migrate plog
	$(MANAGE) createcachetable $(CACHE_TABLE)

dumpezsettings:
	python ./manage.py dumpdata ezconf.ezsettingsdata > ./ezconf/fixtures/initial_data.json
	python ./manage.py dumpcurrentsettings > ./ezconf/ezsettings.json

makemessages:
	$(MANAGE) makemessages -i '*django/*' -l zh_CN

collectstatic:
	[ -d static ] || mkdir static
	$(MANAGE) compress
	$(MANAGE) collectstatic
