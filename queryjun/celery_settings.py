import os


rabbitmq_user = os.environ['RABBITMQ_USER']
rabbitmq_password_hashed = os.environ['RABBITMQ_PASSWORD_HASHED']

CELERY_BROKER_URL = f'pyamqp://{rabbitmq_user}:{rabbitmq_password_hashed}@rabbitmq:5672//'
CELERY_RESULT_BACKEND = 'rpc://'
