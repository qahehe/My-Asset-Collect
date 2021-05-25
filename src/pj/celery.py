"""
@author: chl
@time: 2021.5.1
"""
from __future__ import absolute_import
from celery import Celery
import os,time
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

app = Celery('pj',broker='redis://:123456@127.0.0.1:6379',
        backend='redis://:123456@127.0.0.1:6379/0',
        include=['pj.tasks'])
if __name__ == '__main__':
        app.start()
