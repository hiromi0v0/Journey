from django.db import models

from accounts.models import CustomUser

class Category(models.Model):
    title=models.CharField(verbose_name='カテゴリ',max_length=20)

    def __str__(self):
        return self.title

class PhotoPost(models.Model):

    user=models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.CASCADE)
    country=models.ForeignKey(Country,verbose_name='国',on_delete=models.PROTECT)
    situation=models.OneToOneField(Situation,verbose_name='状況',on_delete=models.PROTECT)
    days1=models.ImageField(verbose_name='状況')
    days2=models.ImageField(verbose_name='状況')



    comment=models.TextField(verbose_name='コメント',)
    image1=models.ImageField(verbose_name='イメージ1',upload_to='photos')
    image2=models.ImageField(verbose_name='イメージ2',upload_to='photos',blank=True,null=True)
    posted_at=models.DateTimeField(verbose_name='投稿日時',auto_now_add=True)

    def __str__(self):
        return self.title


class Situation(models.Model):

    country=models.ForeignKey(Country,verbose_name='国',on_delete=models.PROTECT)
    stress=models.PositiveIntegerField(verbose_name='ストレス')

    def __str__(self):
        return self.title


class Country(models.Model):

    title=models.CharField(verbose_name='インド',max_length=200)


    def __str__(self):
        return self.title