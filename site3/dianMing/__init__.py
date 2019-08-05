print("加载了一次")
with open('./dianMing/users','r',encoding='utf-8') as fs:
        users = [user for user in fs]