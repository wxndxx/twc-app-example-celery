from celery import Celery
import os

RABBIT_USER = os.getenv('RABBIT_USER')
RABBIT_PASSWORD = os.getenv('RABBIT_PASSWORD')
RABBIT_IP = os.getenv('RABBIT_IP')

app = Celery('tasks', broker=f'pyamqp://{RABBIT_USER}:{RABBIT_PASSWORD}@{RABBIT_IP}//')


@app.task
def add(x, y):
    return x + y
