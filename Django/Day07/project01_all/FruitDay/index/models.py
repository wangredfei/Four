from django.db import models

# Create your models here.
class Users(models.Model):
    uphone = models.CharField(max_length=11,verbose_name='手机号码')
    upwd=models.CharField(max_length=200,verbose_name='密码')
    uemail=models.EmailField(verbose_name='电子邮件')
    uname=models.CharField(max_length=20,verbose_name='用户名')
    isActive=models.BooleanField(default=True,verbose_name='活动用户')

    class Meta:
        db_table = "users"
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

# 商品类型Models - GoodsType
class GoodsType(models.Model):
    title=models.CharField(
        max_length=50,
        verbose_name='类型名称'
    )
    picture = models.ImageField(
        upload_to='static/upload/goodstype',
        null=True,
        verbose_name='类型图片'
    )
    desc = models.TextField(
        verbose_name='类型描述'
    )

    def __str__(self):
        return self.title

    def to_dict(self):
        dic = {
            'title': self.title,
            'picture': self.picture.__str__(),
            'desc': self.desc
        }
        return dic


    class Meta:
        db_table = 'goods_type'
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name

#商品Models
class Goods(models.Model):
    title=models.CharField(
        max_length=50,
        verbose_name='商品名称'
    )
    price=models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name='商品价格'
    )
    spec = models.CharField(
        max_length=30,
        verbose_name='商品规格'
    )
    picture = models.ImageField(
        upload_to='static/upload/goods',
        null=True,
        verbose_name='商品图片'
    )
    goodsType = models.ForeignKey(
        GoodsType,
        verbose_name='商品类型'
    )
    isActive = models.BooleanField(
        default=True,
        verbose_name='是否上架'
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name







