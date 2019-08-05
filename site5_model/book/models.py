from django.db import models
class Book(models.Model):
    name = models.CharField(max_length=30,db_column='title')
    author = models.CharField(max_length=30)
    isDelete = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=9,decimal_places=2,default=0.00)
    class Meta:
        #对模型进行描述
        db_table = "book"  #设置真实表的表名
    def __str__(self):
        # print()打印对象是调用该方法，返回字符串说明
        return "<Book {}>".format(self.name)