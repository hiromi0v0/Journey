from django.forms import ModelForm
from django import forms
from .models import PhotoPost
from .models import Attribute


class PhotoPostForm(ModelForm):

    class Meta:
        model=PhotoPost
        fields=['country','title','comment','itinerary','days1','days2','season1','season2','image1','image2','image3','image4']


class AttributeForm(ModelForm):

    class Meta:
        model=Attribute
        fields=['stress','happy','energy','astray','tired','adventure','nature','architecture','healing','instagram','girls','food','art']


class ReligionForm(forms.Form):
    
    religion=forms.fields.ChoiceField(
        choices = (
            ('christian', 'キリスト教'),
            ('hinduism', 'ヒンドゥー教'),
            ('uk', '仏教'),
            ('ch', '中国'),
            ('kr', '韓国'),
        ),
        required=True,
        widget=forms.widgets.Select
    )