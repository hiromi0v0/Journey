from django.db import models

from accounts.models import CustomUser



class PhotoPost(models.Model):

    user=models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.CASCADE)
    country=models.ForeignKey(Country,verbose_name='国',on_delete=models.PROTECT)
    title=models.CharField(verbose_name='タイトル',max_length=200)
    comment=models.TextField(verbose_name='コメント')
    itinerary=models.TextField(verbose_name='旅程')
    situation=models.OneToOneField(Attribute,verbose_name='状況',on_delete=models.PROTECT)
    interest=models.OneToOneField(Attribute,verbose_name='興味',on_delete=models.PROTECT)

    days1=models.IntegerField(verbose_name='日数1')
    days2=models.IntegerField(verbose_name='日数2')
    season1=models.IntegerField(verbose_name='時期1')
    season2=models.IntegerField(verbose_name='時期2')
    image1=models.ImageField(verbose_name='イメージ1',upload_to='photos')
    image2=models.ImageField(verbose_name='イメージ2',upload_to='photos',blank=True,null=True)
    image3=models.ImageField(verbose_name='イメージ3',upload_to='photos',blank=True,null=True)
    image4=models.ImageField(verbose_name='イメージ4',upload_to='photos',blank=True,null=True)
    posted_at=models.DateTimeField(verbose_name='投稿日時',auto_now_add=True)

    def __str__(self):
        return self.title


class Attribute(models.Model):

    country=models.ForeignKey(Country,verbose_name='国',on_delete=models.PROTECT)
    stress=models.PositiveIntegerField(verbose_name='ストレス')
    happy=models.PositiveIntegerField(verbose_name='ハッピー')
    energy=models.PositiveIntegerField(verbose_name='エネルギー')
    astray=models.PositiveIntegerField(verbose_name='人生に迷った')
    tired=models.PositiveIntegerField(verbose_name='疲れた')

    adventure=models.PositiveIntegerField(verbose_name='冒険')
    nature=models.PositiveIntegerField(verbose_name='自然')
    architecture=models.PositiveIntegerField(verbose_name='建築物')
    healing=models.PositiveIntegerField(verbose_name='癒し')
    instagram=models.PositiveIntegerField(verbose_name='インスタ映え')
    girls=models.PositiveIntegerField(verbose_name='女子旅')
    food=models.PositiveIntegerField(verbose_name='料理')
    art=models.PositiveIntegerField(verbose_name='芸術')





    def __str__(self):
        return self.title


class Country(models.Model):

    country_name=models.CharField(verbose_name='国名',max_length=30)
    language1=models.CharField(verbose_name='言語1',max_length=20)
    language2=models.CharField(verbose_name='言語2',max_length=20)
    language3=models.CharField(verbose_name='言語3',max_length=20)
    religion1=models.CharField(verbose_name='宗教1',max_length=20)
    religion2=models.CharField(verbose_name='宗教2',max_length=20)
    religion3=models.CharField(verbose_name='宗教3',max_length=20)
    comment=models.TextField(verbose_name='コメント')
    image=models.ImageField(verbose_name='イメージ',upload_to='photos')
    map=models.TextField(verbose_name='Google_MAP')
    flight=models.TextField(verbose_name='skyscanner')






    def __str__(self):
        return self.country_name