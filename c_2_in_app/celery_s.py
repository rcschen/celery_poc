from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('gg',
             broker='amqp://',
             backend='amqp://',
#             include=['c_2_in_app.tasks'])
             include=['c_2_in_app.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)
import sys
if __name__ == '__main__':
    print '>>>>' ,sys.argv
    app.start()
