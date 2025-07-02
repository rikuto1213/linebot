# your_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('post/create/', views.create_post, name='create_post'),  # 作成
    path('post/edit/<int:post_id>/', views.edit_post, name='edit_post'),  # 修正
    path('post/', views.read_post, name='read_post'),   # 一覧表示
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),   # 削除
    
    path('post/postpic/',views.Pic_post,name='pic_post')
=======
    path('upload/', views.upload_image, name='upload_image'),
    path('images/', views.image_list, name='image_list'),
>>>>>>> new
]
