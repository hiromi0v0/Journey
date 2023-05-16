from django.forms import ModelForm
from django import forms
from .models import PhotoPost,Attribute


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
            ('buddhism', '仏教'),
            ('islam', 'イスラム教'),
            ('judaism', 'ユダヤ教'),
            ('caodaism', 'カオダイ教'),
            ('taoism', '道教'),
            ('mormonism', 'モルモン教'),
            ('etcetera', 'その他'),
        ),)

    language=forms.fields.ChoiceField(
        choices = (
            ('english', '英語'),
            ('chinese', '中国語'),
            ('spanish', 'スペイン語'),
            ('arabic', 'アラビア語'),
            ('french', 'フランス語'),
            ('hindi', 'ヒンドゥー語'),
            ('uzbek', 'ウズベク語'),
            ('vietnamese', 'ベトナム語'),
            ('russian', 'ロシア語'),
            ('icelandic', 'アイスランド語'),
            ('polish', 'ポーランド語'),
            ('bengali', 'ベンガル語'),
            ('khmer', 'クメール語'),
            ('tajik', 'タジク語'),
            ('quichua', 'ケチュア語'),
            ('aymara', 'アイマラ語'),
            ('taiwanese', '台湾語'),
            ('hakka', '客家語'),
            ('etcetera', 'その他'),



        ),

        required=True,
        widget=forms.widgets.Select
    )


# 状況を選ぶフォーム
class SituationForm(forms.Form):
    JUDGE = (('zero', '0'),
        ('one', '1'),
        ('two', '2'),
        ('three', '3'),
        ('four', '4'),
        ('five', '5'))
    
    
    stress=forms.ChoiceField(label='ストレス度',choices=JUDGE,widget=forms.widgets.RadioSelect)
    happy=forms.ChoiceField(label='ハッピー度',choices=JUDGE,widget=forms.widgets.RadioSelect)
    energy=forms.ChoiceField(label='エネルギーがある',choices=JUDGE,widget=forms.widgets.RadioSelect)
    astray=forms.ChoiceField(label='人生迷子度',choices=JUDGE,widget=forms.widgets.RadioSelect)
    tired=forms.ChoiceField(label='疲労度',choices=JUDGE,widget=forms.widgets.RadioSelect)


# 興味を選ぶフォーム
class InterestForm(forms.Form):
    JUDGE = (('zero', '0'),
        ('one', '1'),
        ('two', '2'),
        ('three', '3'),
        ('four', '4'),
        ('five', '5'))
    
    adventure=forms.ChoiceField(label='冒険',choices=JUDGE,widget=forms.widgets.RadioSelect)
    nature=forms.ChoiceField(label='自然',choices=JUDGE,widget=forms.widgets.RadioSelect)
    architecture=forms.ChoiceField(label='建物',choices=JUDGE,widget=forms.widgets.RadioSelect)
    healing=forms.ChoiceField(label='癒し',choices=JUDGE,widget=forms.widgets.RadioSelect)
    instagram=forms.ChoiceField(label='インスタ映え',choices=JUDGE,widget=forms.widgets.RadioSelect)
    girls=forms.ChoiceField(label='女子旅',choices=JUDGE,widget=forms.widgets.RadioSelect)
    food=forms.ChoiceField(label='食事',choices=JUDGE,widget=forms.widgets.RadioSelect)
    art=forms.ChoiceField(label='芸術',choices=JUDGE,widget=forms.widgets.RadioSelect)