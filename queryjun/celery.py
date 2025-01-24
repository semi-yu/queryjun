import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'queryjun.settings')

app = Celery('queryjun')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
