from __future__ import absolute_import
from pj.celery import app
import time

@app.task
def add(a,b):
    return a+b
