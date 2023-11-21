from django.shortcuts import render, redirect
from .models import *
from .forms import *


def main_page(request):
    posts = Post.objects.all()
    if 'tag' in request.GET:
        posts = Post.objects.filter(tag_list__name=request.GET['tag'])
    context = {
        'title': 'Main page',
        'posts': posts,
    }
    return render(request, 'main/index_main.html', context=context)


def post_page(request, post_slug):
    post = Post.objects.get(slug=post_slug)

    if request.method == 'POST':
        if 'delete' in request.POST:
            Post.objects.get(slug=request.POST['delete']).delete()
            return redirect('main_page')
        if 'edit' in request.POST:
            return redirect('edit_page', post.slug)

    context = {
        'title': 'Post page',
        'post': post,
    }
    return render(request, 'main/index_post.html', context=context)


def add_post_page(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            tag_list = form.cleaned_data['tag_list']
            likes = form.cleaned_data['likes']

            instance = Post.objects.create(name=name,
                                           title=title,
                                           text=text,
                                           likes=likes)
            instance.save()
            for i in tag_list:
                instance.tag_list.add(i.pk)

            return redirect('main_page')
    context = {
        'title': 'Add page',
        'form': form,
    }

    return render(request, 'main/index_add.html', context=context)


def edit_post_page(request, edit_slug):
    post = Post.objects.get(slug=edit_slug)
    form = PostForm(initial={'name': post.name,
                             'title': post.title,
                             'text': post.text,
                             'tag_list': post.tag_list.all().values_list('pk', flat=True),
                             'likes': post.likes})

    # [i.pk for i in post.tag_list.all()]
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.name = form.cleaned_data['name']
            post.title = form.cleaned_data['title']
            post.text = form.cleaned_data['text']
            post.tag_list.set(form.cleaned_data['tag_list'])
            post.likes = form.cleaned_data['likes']
            post.save()

            return redirect('main_page')

    return render(request, 'main/index_edit.html', {'form': form})
