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
            ('英語', '英語'),
            ('中国語', '中国語'),
            ('スペイン語', 'スペイン語'),
            ('アラビア語', 'アラビア語'),
            ('フランス語', 'フランス語'),
            ('ヒンドゥー語', 'ヒンドゥー語'),
            ('ウズベク語', 'ウズベク語'),
            ('ベトナム語', 'ベトナム語'),
            ('ロシア語', 'ロシア語'),
            ('アイスランド語', 'アイスランド語'),
            ('ポーランド語', 'ポーランド語'),
            ('ベンガル語', 'ベンガル語'),
            ('クメール語', 'クメール語'),
            ('タジク語', 'タジク語'),
            ('ケチュア語', 'ケチュア語'),
            ('アイマラ語', 'アイマラ語'),
            ('台湾語', '台湾語'),
            ('客家語', '客家語'),
            ('others', 'その他・特になし'),
        ),
        required=True,
        widget=forms.widgets.Select
    )




class ReligionForm(forms.Form):

    religion=forms.fields.ChoiceField(
        choices = (
            ('キリスト教', 'キリスト教'),
            ('ヒンドゥー教', 'ヒンドゥー教'),
            ('仏教', '仏教'),
            ('イスラム教', 'イスラム教'),
            ('ユダヤ教', 'ユダヤ教'),
            ('カオダイ教', 'カオダイ教'),
            ('道教', '道教'),
            ('モルモン教', 'モルモン教'),
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