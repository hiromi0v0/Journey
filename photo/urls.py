from django.urls import path
from .import views


app_name='photo'

urlpatterns=[
    ####################################クラス用#########################################

    path('',views.IndexView.as_view(),name='index'),
    # Formを二つ作ったので、関数で書いた
    path('post/',views.create_photo_view,name='post'),
    path('post_done/',views.PostSuccessView.as_view(),name='post_done'),
    path('photos/<int:country>',views.CountryView.as_view(),name='photos_cat'),
    path('user-list/<int:user>',views.UserView.as_view(),name='user_list'),
    path('photo-detail/<int:pk>',views.DetailView.as_view(),name='photo_detail'),
    path('mypage/',views.MypageView.as_view(),name='mypage'),
    # path('photo/<int:pk>/delete/',views.PhotoDeleteView.as_view(),name='photo_delete'),
    # path('photo/<int:pk>/update/',views.PhotoUpdateView.as_view(),name='photo_update'),


    ################################関数用.as_view(),を取る###############################
#     path('',views.index_view,name='index'),
#     path('photos/<int:category>',views.category_view,name='photos_cat'),
#     path('user-list/<int:user>',views.user_view,name='user_list'),
#     path('mypage/',views.mypage_view,name='mypage'),
]