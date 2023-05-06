from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def Home (request):
    template_name = 'home.html'
    blog_info = Blog_info.objects.first()
    context = {'blog_info':blog_info}
    return render(request, template_name, context)


def Blog(request):
    template_name = 'Blog/blog.html'
    queryset = BlogPost.objects.filter(status='pubished').order_by('-pub_date')
    per_page = 3
    paginator = Paginator(queryset,per_page)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    blog_section = Blog_section.objects.first()
    blog_info = Blog_info.objects.first()
    context = {'posts':posts, 'blog_section':blog_section, 'blog_info': blog_info}
    return render(request, template_name, context)


def Single_post(request,post_slug):
    template_name = 'Blog/single.html'
    post = get_object_or_404(BlogPost, slug = post_slug )
    context = {'post':post}
    return render(request, template_name, context)

def category_details(request, category_slug):
    template_name = 'Blog/category.html'	
    category_url = get_object_or_404(Category, slug = category_slug)
    queryset = BlogPost.objects.filter(category = category_url, status = 'pubished').order_by('-pub_date')
    per_page = 3
    paginator = Paginator(queryset,per_page)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    blog_section = Blog_section.objects.first()
    context = {'posts': posts, 'blog_section':blog_section}
    return render(request, template_name, context)




