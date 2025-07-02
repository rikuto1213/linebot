<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from bot_app.models import Post
from bot_app.models import Picture
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import os
#URLと処理を関連付けるビューを定義



def Pic_post(request):
    

    pic_post=Picture()#ここまでは実行できてる.
    print("s")
    if request.method =='GET':
        
        

        form=PostForm(request.POST,instance=pic_post)

        return redirect('bot_app:read_post')
    
        if form.is_valid():
            # チェック結果に問題なければデータを作成する
            pic_post = form.save(commit=False)
            pic_post.save()

        
=======
# your_app/views.py
import base64
from django.shortcuts import render, redirect
from .models import ImageData
from .forms import UploadImageForm
>>>>>>> new

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES['image']
            image_name = image_file.name
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            ImageData.objects.create(name=image_name, image_base64=encoded_image)
            return redirect('image_list')
    else:
        form = UploadImageForm()
    return render(request, 'bot_app/upload.html', {'form': form})

<<<<<<< HEAD
        return redirect('bot_app:read_post')


def read_post(request):
    """
    データの一覧を表示する
    """
    # 全オブジェクトを取得
    posts = Post.objects.all().order_by('id')
    return render(request,
                  'bot_app/post_list.html',  # 呼び出す Template
                  {'posts': posts})  # Template に渡すデータ


def edit_post(request, post_id):
    """
    対象のデータを編集する
    """
    # IDを引数に、対象オブジェクトを取得
    post = get_object_or_404(Post, pk=post_id)

    # ページロード時
    if request.method == 'GET':
        # 対象オブジェクトにより form を作成
        form = PostForm(instance=post)

        # ページロード時は form とデータIDを Template に渡す
        return render(request,
                      'bot_app/post_form.html',  # 呼び出す Template
                      {'form': form, 'post_id': post_id})  # Template に渡すデータ

    # 実行ボタン押下時
    elif request.method == 'POST':
        # POST されたデータにより form を作成
        form = PostForm(request.POST, instance=post)

        # 入力されたデータのバリデーション
        if form.is_valid():
            # チェック結果に問題なければデータを更新する
            post = form.save(commit=False)
            post.save()

        # 実行ボタン押下時は処理実行後、一覧画面にリダイレクトする
        return redirect('bot_app:read_post')


def delete_post(request, post_id):
    # 対象のオブジェクトを取得
    post = get_object_or_404(Post, pk=post_id)
    post.delete()

    # 削除リクエスト時は削除実行後、一覧表示画面へリダイレクトする
    return redirect('bot_app:read_post')

def savepic():
    print("hozon")
    

class PostForm(ModelForm):
    """
    フォーム定義
    """
    class Meta:
        model = Post
        # fields は models.py で定義している変数名
        fields = ('name', 'micropost')
=======
def image_list(request):
    images = ImageData.objects.all()
    return render(request, 'bot_app/image_list.html', {'images': images})
>>>>>>> new
