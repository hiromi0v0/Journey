from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,FormView
# from django.core.paginator import Paginator

# # 写真投稿ページ系
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import PhotoPostForm,AttributeForm,SituationForm,InterestForm,LanguageForm,ReligionForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# # ------------トップページ写真投稿
from .models import PhotoPost,Attribute,Country
# # ------------詳細ページ
from django.views.generic import DetailView,UpdateView
# # ページを削除する
# from django.views.generic import DeleteView

# # 関数用ページネーション
# from django.core.paginator import Paginator
# # 関数用Categoryモデル
# from .models import Category
# from django.shortcuts import get_object_or_404
# # 関数用
# from django.shortcuts import redirect


# #################################################################################
#                                 #クラス
# #################################################################################
# 診断トップページ
class IndexView(TemplateView):

    template_name='index.html'


# -----------------------------situation：状況の選択ページ---------------------------------
def situation(request):
# ➁➀でformを空にして、ユーザーに選択してもらう＝POST送信でデータが送られる。
    # HTTPリクエストがPOSTだったら、
    if request.method == 'POST':
        # ユーザーが入力したデータがフォームに入る
        form = SituationForm(request.POST)
# もし入力内容がOKだったら
        if form.is_valid():
            request.session['attribute'] = {}  # 辞書として初期化

            # request.session['attribute'] = []
# 各項目のデータをセッションに保存する！
# セッションにデータ（文字列・値）を入れる場合の構文：
# request.session['セッション名'] = データ
# まず、formの各項目をfor文でsituation_fieldに一つずつ入れて、セッションに保存する。
            for situation_field in ['stress', 'happy', 'energy', 'astray', 'tired']:
                request.session['attribute'][situation_field] = int(form.cleaned_data[situation_field])
            print(request.session.get('attribute'))
                # request.session['attribute'].append(int(form.cleaned_data[situation_field]))
# セッションの内容が保存できているかprintして確認する。
            # print(request.session['attribute'])
            print(request.session['attribute']['energy'])

# 入力内容に問題がなければ、次のページに飛ぶよ
            return redirect('photo:interest')
    else:
# ➀get送信でデータが来た時(ユーザーが初めてページに遷移してきた時)に、Formを空にする
        form = SituationForm()
        # {'form': form}は、{'happy': 1}みたいなデータが入っている。
    return render(request, 'situation.html', {'form': form})


# --------------------------------interest:興味の選択ページ------------------------------------

def interest(request):
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():

            for interest_field in ['adventure', 'nature', 'architecture', 'healing', 'instagram', 'girls', 'food', 'art']:
                request.session['attribute'][interest_field] =int(form.cleaned_data[interest_field])
                # request.session['attribute'].append(int(form.cleaned_data[interest_field]))
            print(request.session.get('attribute'))
            # print(request.session['attribute']['energy'])

# 入力内容に問題がなければ、次のページに飛ぶよ
            return redirect('photo:language')
    else:
        form = InterestForm()
    return render(request, 'interest.html', {'form': form})


#--------------------------------------LanguageForm:言語選択ページ-----------------------------------------

def language(request):
    # HTTPリクエストがPOSTだったら、
    if request.method == 'POST':
        # ユーザーが入力したデータがフォームに入る
        form = LanguageForm(request.POST)
        # もし入力内容がOKだったら
        if form.is_valid():
            # フォームで選んだ言語の情報をセッションに保存する
            request.session['language'] = form.cleaned_data['language']
            # print(request.session['attribute'])
            print(request.session.get('language'))
            # 入力内容に問題がなければ、次のページに飛ぶよ
            return redirect('photo:religion')
    else:
        form = LanguageForm()
    return render(request, 'language.html', {'form': form})

#--------------------------------------宗教選択ページ--------------------------------------

def religion(request):
    if request.method == 'POST':
        form = ReligionForm(request.POST)
        if form.is_valid():
            # 宗教の情報をセッションに保存する
            request.session['religion'] = form.cleaned_data['religion']

# 入力内容に問題がなければ、次のページに飛ぶよ
            return redirect('photo:recommend')
    else:
        form = ReligionForm()
    return render(request, 'religion.html', {'form': form})


#---------------------------------------------結果表示ページ--------------------------------------
def recommend(request):
    # 各ページに保存したセッションからデータを取ってくる
    # 構文：request.session.get('セッション名')をそれぞれの変数に入れている。
    print(request.session.get('attribute'))
    print(request.session['attribute'])
    attribute_list = []
    for value in request.session.get('attribute').values():
        attribute_list.append(value)
    print(attribute_list)
    print(request.session.get('language'))
    print(request.session.get('religion'))

    attribute_session = request.session.get('attribute')
    language_session = request.session.get('language')
    religion_session = request.session.get('religion')

# 各セッションの情報をsession_listに保存する。
    # session_list = [attribute, language_session, religion_session]
# ちゃんとデータが入っているか確認する。多分来てない。
    # print(session_list)

# Attributeのデータベースをすべて取得する＝投稿ページで登録されたhappy:1みたいな情報。
# 変数名attribute_dbはAttributeのデータベース全部の情報が入っている。
    attribute_db=Attribute.objects.all()

# country_id毎の属性の合計値を出し、country_idの項目数で割る。
    for attribute in attribute_db:


        return render(request, 'recommend.html')







# -----------------------------------------写真投稿ページ-------------------------------------------
def create_photo_view(request):
    if request.method == 'POST':

        photo_post_form = PhotoPostForm(request.POST,request.FILES)
        attribute_form = AttributeForm(request.POST)

        forms = (photo_post_form, attribute_form)

        if photo_post_form.is_valid() and attribute_form.is_valid:
            attribute = attribute_form.save(commit=False)
            attribute.country = photo_post_form.cleaned_data['country']
            attribute.save()

            photo_post = photo_post_form.save(commit=False)
            photo_post.attribute = attribute
            photo_post.user = request.user  # ユーザーを設定
            photo_post.save()

            return redirect(to='/')

    else:
        forms = (PhotoPostForm(), AttributeForm())

    param = {
        'forms': forms
    }

    return render(request, 'post_photo.html', param)






@method_decorator(login_required,name='dispatch')
class PostSuccessView(TemplateView):
    template_name='post_success.html'

# # 写真投稿一覧表示
class IndexView(ListView):
    template_name='index.html'
    queryset=PhotoPost.objects.order_by('posted_at')


# ページネーション
    paginate_by=9

class CountryView(ListView):
    template_name='index.html'
    paginate_by=9

    def get_queryset(self):
        country_id=self.kwargs['country']
        countrys=PhotoPost.objects.filter(country=country_id).order_by('-posted_at')

        return countrys


class UserView(ListView):
    template_name='index.html'
    paginate_by=9

    def get_queryset(self):

        user_id=self.kwargs['user']
        user_list=PhotoPost.objects.filter(user=user_id).order_by('-posted_at')

        return user_list


# # ------------詳細ページ作成
class DetailView(DetailView):
    template_name='detail.html'
    model=PhotoPost,

# # マイページを用意する

class MypageView(ListView):
    template_name='mypage.html'
    paginate_by=9

    def get_queryset(self):
        queryset=PhotoPost.objects.filter(user=self.request.user).order_by('posted_at')

        return queryset

# # ページを削除する
# class PhotoDeleteView(DeleteView):
#     model=PhotoPost
#     template_name='photo_delete.html'
#     success_url=reverse_lazy('photo:mypage')

# # ページを更新する
# @method_decorator(login_required,name='dispatch')
# class PhotoUpdateView(UpdateView):
#     model=PhotoPost
#     form_class=PhotoPostForm
#     template_name='photo_update.html'
#     success_url=reverse_lazy('photo:post_done')

# ######################################################################################
#                                   #  関数
# ######################################################################################

# # # トップページ表示
# # # ページを表示する関数は必ずrequestがいる
# # def index_view(request):


# # # 一覧データ取得
# # # PhotoPostのDB一覧を降順？でquerysetの中に入れる。
# # # ＤＢから沢山データを持てくる時は基本的にquerysetっていう名前の変数を使う。
# # # PhotoPostっていうデータベースから、ojjectsの検索を使って抽出する。順番（order_by）は、投稿日時の降順('-posted_at')ですよ
# #     queryset=PhotoPost.objects.order_by('-posted_at')



# # ページネーション。
# # 一ページに９件の記事を表示させるよ。
#     # paginator=Paginator(queryset,9)

#     # request.GETはDjangoの機能で、http:のリクエスト?以降のもの情報をゲットできる！
#     # http:wwwwww?page=2とかだったら、2が取れるよ。
#     # get()はrequest.GETだと謎の数字をURLに直接入力されちゃうとエラーになるので設定している。
#     # get('page',1)とすると、pageがある時はpageを、ないときは1を取ってくるよって意味。

#     # page_number=request.GET.get('page',1)

#     # page_obj=paginator.page(page_number)
# # pages=get_django_pagination(queryset,)

# # querysetをcontextに入れるよ。でも、
# # photos_list.htmlの中で、{% for record in object_list %}ってobject_listじゃないと受け取らないよって言ってるし、
# # pagination.htmlで、{%if page_obj.has_previous%}ってpage_objじゃないと受け取らないよって言ってるので、
# # まず、querysetをそれぞれ'object_list'と'page_obj'に入れるよ。
# # しかも第三引数は一単語？じゃないといけないので、さらに二つをcontextに入れるよ。
#     # context = {'object_list': queryset,
#             #    'page_obj':queryset}




# # 答え（return）を出すときに第一引数は、request固定。第二引数はtemplateであるhtml。第三引数はcontext（任意）データ。って決まっている。
# # contextにはデータベース操作をして取得したデータなどを格納します。
# # renderはデータベースのデータなどを反映させたHTMLページを作成して、HTTPレスポンスとしてブラウザに返す役割があるよ。
#     # return render(request,'index.html',context)



# ######################################################################################
#                                   #  関数
# ######################################################################################


# # -------------------------------# トップページ表示 関数-------------------------------
# # ページを表示する関数は必ずrequestがいる。ページに関するものだけ。
# def index_view(request):


# # 一覧データ取得
# # データベースPhotoPost一覧を降順？でquerysetの中に入れる。
# # querysetは名前何でもいい。クラスに合わせてquerysetにした。
#     queryset=PhotoPost.objects.order_by('-posted_at')


# # ページネーション。わからないので保留
# # pages=get_django_pagination(queryset,)

# # Paginatorクラスを使って、全データを１ページ当たり９記事表示させるようにする。
#     paginator=Paginator(queryset,9)

# # request.GETでget送信されたURLから?以下の情報を取得。https:aaaaaaa?page=2だったら、2を持ってくる。

# # 'page'はpagination.htmlで<a class="page-link" href="?page={{num}}">{{num}}</a>。って自分で指定しましたよ。
# # だから値が取れる。
# # getはURLに謎の数字

#     page_number=request.GET.get('page',1)

# # pagesは、1ページあたり9記事のページのデータが入っている。
# # paginator（1ページあたり9記事）.page(page_number)で今いるページのNoを出すっ！
# # メソッド.page(page_number)より.get_page(page_number)
#     pages=paginator.page(page_number)

#     # ページを表示させるための、
# # photos_list.htmlの中で、{% for record in object_list %}ってobject_listじゃないと受け取らないよって言ってるし、
# # pagination.htmlで、{%if page_obj.has_previous%}ってpage_objじゃないと受け取らないよって言ってるので、
# # pagesをそれぞれ、'object_list'と'page_obj'に入れる。
# # しかも第三引数は一単語？じゃないといけないので、さらに二つをcontextに入れる。
#     context = {'object_list': pages,
#                'page_obj':pages}
# # 第一引数は、request。第二引数はhtml。第三引数は表示したいデータ。って決まっている。
#     return render(request,'index.html',context)


# # ---------------------------------# カテゴリ一覧表示 関数---------------------------------

# # ページを表示する関数は必ずrequestがいる
# # Urlsからcategoryっていうキー（４）とかで送られてくる。Pythonの関数復習
# def category_view(request,category):

#     # 一覧データ取得
# # PhotoPostのDB一覧を降順？でquerysetの中に入れる。
# # カテゴリーだけ抽出してquerysetへ入れる。
# # (category(Photopostデータベースの項目名)=category(値。urls.pyから持ってきたid。キー（４。)
#     queryset=PhotoPost.objects.filter(category=category).order_by('-posted_at')
#     paginator=Paginator(queryset,9)
#     page_number=request.GET.get('page',1)
#     # paginator（1ページあたり9記事）.page(page_number)で今いるページのNoを出す！
#     pages=paginator.page(page_number)

#     info_name=get_object_or_404(Category,id=category).title

#     context = {'object_list': pages,
#                'page_obj':pages,
#                'info_name':info_name,
#                }

#     # 第一引数は、request。第二引数はhtml。第三引数は表示したいデータ。って決まっている。

#     return render(request,'index.html',context)


# # -----------------------------------# ユーザー一覧表示 関数-----------------------------------
# # ページを表示する関数は必ずrequestがいる
# def user_view(request,user):

#     # 一覧データ取得

#     queryset=PhotoPost.objects.filter(user=user).order_by('-posted_at')
# # ページネーション
#     paginator=Paginator(queryset,9)
#     page_number=request.GET.get('page',1)
#     pages=paginator.page(page_number)
#     # get_object_or_404はDjandoのデフォルト
#     # info_name=get_object_or_404(CostomUser,id=user).username

#     context = {'object_list': pages,
#                'page_obj':pages,
#             #    'info_name':info_name
#             }

#     # 第一引数は、request。第二引数はhtml。第三引数は表示したいデータ。って決まっている。
#     return render(request,'index.html',context)



# # # ------------------------------------# マイページ 関数-------------------------------------
# @login_required(login_url='/login/')
# def mypage_view(request):

#     # 一覧データ取得。request.userで、ログインしているユーザーを抽出する。
#     # request.userにselfはいらない。selfはクラス用だから今回はいらない。
#     queryset=PhotoPost.objects.filter(user=request.user).order_by('-posted_at')

# # レコードの数を.coount()でカウント
#     # record_count=queryset.coount()

# # ページネーション
#     paginator=Paginator(queryset,9)
#     page_number=request.GET.get('page',1)
#     pages=paginator.page(page_number)
#     # contextのデータがhtmlに送られる
#     context = {'object_list': pages,
#                'page_obj':pages,
#                'queryset':queryset}

#     return render(request,'mypage.html',context)


# # --------------------------------------# 記事投稿 関数---------------------------------------
# # # ログインしている場合
# @login_required(login_url='/login/')
# def createPhoto_view(request):


# # # GETの時（一番最初にページを開いたとき＝フォームに何も入っていない時）
#     if request.methood == 'GET':
# #     # PhotoPostForm()空のフォームだよ。
#         form=PhotoPostForm()
# # # POSTの時(フォームに色々と入力して投稿ボタンをおした時)
# # # 送信データを押すと、基本的にrequest.POSTにすべてのデータが入る（DBにはまだ入ってないよ）
# # # request.POST['name']とかで取りだせる。
# # # 送信データを押すと、添付ファイルはrequest.FILESにデータが入る。
# # # （バリデーションが通らなくても空にならない。）
#     else:
#         form=PhotoPostForm(request.POST,request.FILES)
# #         # バリエーションが通った時
#         if form.is_valid():
# #             # フォームのデータを仮保存
#             poatdata=form.save(commit=False)
# #             # userの情報を足す
#             poatdata.user=request.user
# #             # そして全部まとめて保存。ここで次のページに行く。
#             postdata.save()
# # redirectの機能をimportした。
#             return redirect('photo:post_done')


# #         # 送信データ
#         context={'form':form}
#         return render(request,'post_photo.html,context')


# # # 記事詳細
# # def detailPhoto_view(request,photo_id):

# #     # 詳細データ
# #     object=get_object_or_404(PhotoPost,id=photo_id)
# #     # 送信データ
# #     # 1レコード分をobjectに入れて
# #     context={'object':object}

