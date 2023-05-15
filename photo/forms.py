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

class JudgeForm(forms.Form):

    religion=forms.fields.ChoiceField(
        choices = (
            ('stress', 'ストレス'),
            ('happy', 'ハッピー'),
            ('energy', 'エネルギー'),
            ('astray', '人生迷子'),
            ('tired', '疲労度'),
            ('adventure', '冒険'),
            ('nature', '自然'),
            ('architecture', '建物'),
            ('healing', '癒し'),
            ('instagram', 'インスタ映え'),
            ('girls', '女子旅'),
            ('food', '食事'),
            ('art', '芸術'),


        ),

        required=True,
        widget=forms.widgets.Select
    )

