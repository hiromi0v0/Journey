from django.db import models

from accounts.models import CustomUser

class Country(models.Model):

    country_name=models.CharField(verbose_name='国名',max_length=50)
    language1=models.CharField(verbose_name='言語1',max_length=50)
    language2=models.CharField(verbose_name='言語2',max_length=50,blank=True,null=True)
    language3=models.CharField(verbose_name='言語3',max_length=50,blank=True,null=True)
    religion1=models.CharField(verbose_name='宗教1',max_length=50)
    religion2=models.CharField(verbose_name='宗教2',max_length=50,blank=True,null=True)
    religion3=models.CharField(verbose_name='宗教3',max_length=50,blank=True,null=True)
    comment=models.TextField(verbose_name='コメント')
    image=models.ImageField(verbose_name='イメージ',upload_to='country_photos')
    map=models.TextField(verbose_name='Google_MAP')
    flight=models.TextField(verbose_name='skyscanner',blank=True,null=True)

    def __str__(self):
        return self.country_name




class Attribute(models.Model):

    country=models.ForeignKey(Country,verbose_name='国',on_delete=models.PROTECT)
    stress=models.FloatField(verbose_name='ストレス')
    happy=models.FloatField(verbose_name='ハッピー')
    energy=models.FloatField(verbose_name='エネルギー')
    astray=models.FloatField(verbose_name='人生に迷った')
    tired=models.FloatField(verbose_name='疲れた')

    adventure=models.FloatField(verbose_name='冒険')
    nature=models.FloatField(verbose_name='自然')
    architecture=models.FloatField(verbose_name='建築物')
    healing=models.FloatField(verbose_name='癒し')
    instagram=models.FloatField(verbose_name='インスタ映え')
    girls=models.FloatField(verbose_name='女子旅')
    food=models.FloatField(verbose_name='料理')
    art=models.FloatField(verbose_name='芸術')


    def __str__(self):
        return self.happy




class PhotoPost(models.Model):

    user=models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.CASCADE)
    country=models.ForeignKey(Country,verbose_name='国',on_delete=models.PROTECT)
    title=models.CharField(verbose_name='タイトル',max_length=200)
    comment=models.TextField(verbose_name='コメント')
    itinerary=models.TextField(verbose_name='旅程')
    attribute=models.OneToOneField(Attribute,verbose_name='属性',on_delete=models.PROTECT)

    days1=models.IntegerField(verbose_name='最短日程')
    days2=models.IntegerField(verbose_name='最長日程')
    season1=models.IntegerField(verbose_name='時期1')
    season2=models.IntegerField(verbose_name='時期2')
    image1=models.ImageField(verbose_name='イメージ1',upload_to='post_photos')
    image2=models.ImageField(verbose_name='イメージ2',upload_to='post_photos',blank=True,null=True)
    image3=models.ImageField(verbose_name='イメージ3',upload_to='post_photos',blank=True,null=True)
    image4=models.ImageField(verbose_name='イメージ4',upload_to='post_photos',blank=True,null=True)
    posted_at=models.DateTimeField(verbose_name='投稿日時',auto_now_add=True)
    update_at=models.DateTimeField(verbose_name='変更日時',auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.country})"


