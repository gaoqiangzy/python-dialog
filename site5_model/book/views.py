from django.http import HttpResponse
from django.shortcuts import render
import cgitb
cgitb.enable()
# Create your views here.
from book.models import Book


def index(request):
    '''
    操作rom
    1.所有的模型类都有个objects属性，就是一个manager对象，用于进行数据操作管理
    2.添加数据
        2.1 模型类。objects.create(属性=值)
                返回生成的对象----》记录
        2.2 添加数据
            对象 = 模型类（）
            对象。属性=值
            对象。save（）保存数据
        2.3 ，模型类。objects.get_or_crate(属性=值)
            如果有就获取，没有就创造
    3查看数据
            模型类。objects.all() 查看所有数据
            模型类。objects.filter(条件)条件查询，相当于where
            模型类。objects.get(条件)只能获取一条数据
    4修改数据
            4.1 模型类。object。filter(条件).update(属性=新属性值)
                一次更新多条
            4.2 先查询出对象  ---一次更新一条
                对象。属性=值
                对象。属性=值
                对象。属性=值
                对象。save()
        5 删除数据
            查询偶delete()
    :param request:
    :return:
    '''
    rs = Book.objects.create(name='红楼梦',author='曹雪芹',price=9.9)
    print(rs)
    book = Book()
    book.name='红楼梦'
    book.author='曹雪芹'
    book.price=99
    book.save()
    book = Book.objects.get_or_create(name='三国演义',author='施耐庵',price=88)
    print(book)

    #查看数据
    # books=Book.objects.all()
    # content = {
    #     "books":books
    # }
    # book = Book.objects.get(id=1)
    # book = Book.objects.get(name='红楼梦')  如果存在多条数据，返回列表[]
    # books = Book.objects.filter(name='红楼梦').first()#获取第一条
    # print(book)

    #更新数据
    # rs = Book.objects.filter(name='红楼梦').update(name='红楼2')
    # print(rs)
    # book = Book.objects.get(id=1)
    # book.name='红楼3'
    # book.save()
    book = Book.objects.get(id=1)
    book.delete()
    return HttpResponse("bookModel")
    # return render(request,"index.html",context=content)