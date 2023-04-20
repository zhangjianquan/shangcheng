from django.db import models

# Create your models here.

# class User(models.Model):
#     username=models.CharField(max_length=20,unique=True)
#     password=models.CharField(max_length=20)
#     mobile=models.CharField(max_length=11,unique=True)
#django自带用户模型，有密码加密和密码验证
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile=models.CharField(max_length=11,unique=True)
    class Meta:
        db_table='tb_users'
        verbose_name='用户管理'
        verbose_name_plural=verbose_name