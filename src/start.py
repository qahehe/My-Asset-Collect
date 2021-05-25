"""
@author: chl
@time: 2021.5.1
"""
import time,os,sys
#import setting
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from pj.tasks import getdomain
from pj.celery import app

id_dict = {}

# 检查多个队列
def check(id_dict,bool):
    id_dict_c = {}
    while True:
        # 循环检查任务，知道所有任务完成
        for key in id_dict.keys():
            if check_one(key,bool) == 'None':
                id_dict_c[key] = id_dict[key]
            time.sleep(3)

        if id_dict_c:
            id_dict = copy.copy(id_dict_c)
            id_dict_c = {}

        else:
            print('all done')
            return

def check_one(id,bool):
    if bool == 'domain':
        mark = 'domain'
    else:
        mark = 'IP' if bool == 'ip' else 'C scan'
    async_task = AsyncResult(id=id,app=app)
    if async_task.successful():
        result = async_task.get()

        if mark != 'C scan':
            print('[-]:{} sub task done({})'.format(mark,id))

        return 'done'
    else:
        if mark != 'C scan':
            print('[-]:{} sub task None({})'.format(mark, id))
        return 'None'

# 在备案domain中获取每个域名，每50个域名对应一个任务ID
# 返回任务ID与域名列表相对应的字典
def getsubdomain():
    id_dict = {}
    target_list = []
    thread_num = 50
    count = 0
    with open(setting.ROOT_PATH +'/data/domain.txt','r',encoding='utf-8') as f:
        target = f.readline().strip('\n')
        while target:
            target_list.append(target)
            count += 1
            if count == thread_num:
                count = 0
                res = getdomain.delay(target_list)
                id_dict[res.id] = target_list
                target_list = []
            target = f.readline().strip('\n')
        if target_list:
            res = getdomain.delay(target_list)
            id_dict[res.id] = target_list

    return id_dict


if __name__ == '__main__':
    os.system('celery --app=pj worker -l INFO')
    start_time = time.time()
    id_dict = getsubdomain() #get subdomain task
    check(id_dict, 'domain') #monitor subdomain task
    end_time = time.time()
    print('time cost:', "{:.5}".format(end_time - start_time), 'seconds.')
