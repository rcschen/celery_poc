from __future__ import absolute_import, unicode_literals
from celery import Celery
from const import *
app = Celery('workers',
#             broker=RABBITMQ,
#             backend=RABBITMQ)
             broker='amqp://',
             backend='amqp://',
             include=['workers.tasks'])

app.conf.update(
    result_expires=3600,
)

