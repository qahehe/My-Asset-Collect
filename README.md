# My-Asset-Collect
这是一个简单的基于Python的资产收集工具，它使用了celery和redis来实现异步任务管理。
我在windows10下的子系统Ubuntu20.04LTS下编写
还在编写中，预计在5.3号内完成

# Usage
1.安装python ---under python3.6
最好是python3.6以下的版本，python3.7会有celery开启失败的风险
2.安装celery和redis
pip3 install celery   #现在默认会安装为5.0以上版本
pip3 install redis
pip3 install celery['redis'] #celery的redis依赖安装一下
3.django其实没太多用处，但是装一下吧
pip3 install django
