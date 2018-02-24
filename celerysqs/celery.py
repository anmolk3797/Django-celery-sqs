import os
import typing

from celery import Celery

# set the default django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerysqs.settings')

from django.conf import settings  
app = Celery('celery-sqs') 

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
