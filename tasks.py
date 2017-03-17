from celery import Celery

#app = Celery('tasks', broker='pyamqp://guest@localhost//')
app = Celery('tasks', broker='amqp://',
             backend='amqp://',)
@app.task
def add(x, y):
    print '>>>>>>>'
    return x + y
