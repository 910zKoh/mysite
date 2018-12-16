from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import LoginForm
# Create your views here.

class LoginView(View):
    def get(self, request, *arg, **kwargs):
        """GET リクエスト用のメソッド"""
        context = {
            'form' : LoginForm(),
        }
        # ログイン画面用のテンプレートに値が空のフォームをレンダリング
        return render(request, 'accounts/login.html',context)

    def post(self, request, *arg, **kwargs):
        """POST リクエスト用のメソッド"""
        # リクエストからフォームを作成
        form = LoginForm(request.POST)
        
        # バリデーション(ユーザー認証も合わせて実施)
        if not form.is_valid():
            # バリデーションNGの場合はログイン画面のテンプレートを再表示
            return render(request, 'accounts/login.html', {'form':form})
        
        # Userオブジェクトをフォームから取得
        user = form.get_user()

        # ログイン処理（取得したUserオブジェクトをセッションに保存 & Userデータを更新）
        auth_login(requset, user)

        # ショップ画面にリダイレクト
        return redirect(reverse('shop:index'))

login = LoginView.as_View()
