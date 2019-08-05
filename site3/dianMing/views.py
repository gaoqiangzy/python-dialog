import random
from django.http import HttpResponse
from dianMing import users
def index(request):
    #点名
        # 方式一
        # users = ['张三','李四','王二','麻子']
        #方式二
        # with open('./dianMing/users','r',encoding='utf-8') as fs:
        #     users = [user for user in fs]
        user = random.choice(users)
        return HttpResponse(user)
