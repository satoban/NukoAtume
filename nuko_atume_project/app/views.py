from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(View):

    def get(self, request, *args, **kwarags):
        '''
        ホーム画面を呼び出す
        '''
        post_data = Post.objects.order_by('-id')  # idの降順にデータを取得する
        return render(request, 'index.html',
                      {'post_data': post_data})


class PostDetailView(View):

    def get(self, request, *args, **kwarags):
        '''
        投稿の詳細画面を呼び出す
        '''
        post_data = Post.objects.get(id=self.kwargs['pk'])  # 特定の投稿を取得する
        return render(request, 'post_detail.html',
                      {'post_data': post_data})


class CreatePostView(View):
    def get(self, request, *args, **kwarags):
        '''
        投稿の新規画面を呼び出す
        '''
        form = PostForm(request.POST or None)
        return render(request, 'post_form.html',
                      {'form': form})

    def post(self, request, *args, **kwarag):
        '''
        新規投稿に関する処理
        '''
        form = PostForm(request.POST or None)

        if form.is_vaild():
            post_data = Post()
            post_data.autor = request.user
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.save()  # 作成した投稿内容をデータベースに保存する
            return redirect('post_detail', post_deta.id)

        return render(request, 'post_form.html',
                      {'form': form})


class PostEditView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwarags):
        '''
        投稿の詳細画面を呼び出す
        '''
        post_data = Post.objects.get(id=self.kwargs['pk'])  # 特定の投稿を取得する
        form = PostForm(request.Post or None)
        initial = {'title': post_data.title,
                   'content': post_data.content
                   }
        return render(request, 'post_form.html',
                      {'post_data': post_data})

    def post(self, request, *args, **kwarag):
        '''
        投稿内容を編集する
        '''
        form = PostForm(request.POST or None)
        if form.is_vaild():
            post_data = Post.objects.get(id=self.kwargs['pk'])
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.save()  # 作成した投稿内容をデータベースに保存する
            return redirect('post_detail', self.kwargs['pk'])

        return render(request, 'post_form.html',
                      {'form': form})


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwarags):
        '''
        投稿の削除画面を呼び出す
        '''
        form = PostForm(request.POST or None)
        return render(request, 'post_form.html',
                      {'form': form})

    def post(self, request, *args, **kwarag):
        '''
        投稿内容を削除した後、ホーム画面に遷移する
        '''
        post_data = Post.objects.get(id=self.kwargs['pk'])  # 特定の投稿を取得する
        post_data.delete()
        return redirect('index')
