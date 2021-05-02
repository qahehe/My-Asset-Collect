import time,os,sys
#import setting
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from pj.tasks import add
from pj.celery import app

if __name__=='__main__':
    os.system('celery --app=pj worker -l INFO')
    add.delay(2,8)
    print("hello world")
