"""
@author: chl
@time: 2021.5.1
"""
from __future__ import absolute_import
from pj.celery import app
import os,sys,threading,time
from celery.result import AsyncResult
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.dirname(ROOT_PATH)))
import setting
from Sublist3r import sublist3r
@app.task
def getdomain(target_list):
    threads = []
    # target_list  = ['example.com']
    for target in target_list:
        print(target)
        t = threading.Thread(target=sublist3r.main,
                              args=(target,50, setting.ROOT_PATH + '/data/subdomain/' + target + '.txt',
                                    None,False,True,False,'ssl'))
        threads.append(t)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return 1
