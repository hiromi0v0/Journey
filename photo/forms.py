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




class LanguageForm(forms.Form):
    language = forms.ChoiceField(
        choices=(
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
            ('others', 'その他・特になし'),
        ),
        required=True,
        widget=forms.widgets.Select
    )




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
            ('others', 'その他・特になし'),
        ),

        required=True,
        widget=forms.widgets.Select
    )





# 状況を選ぶフォーム
class SituationForm(forms.Form):
# まず、0から5の段階のラジオボタンの内容を設定する
    JUDGE = (('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'))
    
# RadioSelectはラジオボタンを表示させるためのもの。
    stress=forms.ChoiceField(label='ストレス度',choices=JUDGE,widget=forms.widgets.RadioSelect, initial='0')
    happy=forms.ChoiceField(label='ハッピー度',choices=JUDGE,widget=forms.widgets.RadioSelect, initial='0')
    energy=forms.ChoiceField(label='エネルギーがある',choices=JUDGE,widget=forms.widgets.RadioSelect, initial='0')
    astray=forms.ChoiceField(label='人生迷子度',choices=JUDGE,widget=forms.widgets.RadioSelect, initial='0')
    tired=forms.ChoiceField(label='疲労度',choices=JUDGE,widget=forms.widgets.RadioSelect, initial='0')


# ------------------------------興味を選ぶフォーム
class InterestForm(forms.Form):
    JUDGE = (('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'))
    
    adventure=forms.ChoiceField(label='冒険',choices=JUDGE,widget=forms.widgets.RadioSelect, initial='0')
    nature=forms.ChoiceField(label='自然',choices=JUDGE,widget=forms.widgets.RadioSelect, initial='0')
    architecture=forms.ChoiceField(label='建物',choices=JUDGE,widget=forms.widgets.RadioSelect, initial='0')
    healing=forms.ChoiceField(label='癒し',choices=JUDGE,widget=forms.widgets.RadioSelect, initial='0')
    instagram=forms.ChoiceField(label='インスタ映え',choices=JUDGE,widget=forms.widgets.RadioSelect, initial='0')
    girls=forms.ChoiceField(label='女子旅',choices=JUDGE,widget=forms.widgets.RadioSelect, initial='0')
    food=forms.ChoiceField(label='食事',choices=JUDGE,widget=forms.widgets.RadioSelect, initial='0')
    art=forms.ChoiceField(label='芸術',choices=JUDGE,widget=forms.widgets.RadioSelect, initial='0')