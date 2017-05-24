from django.shortcuts import render, redirect
from .models import *


def index(request):
    # a=Book.objects.create(title='The Great Gatsby', author='F scotty fitzgeraldson', published_date='1993-03-11')

    # print a.published_date, b.title, c.title
    context = {
    "books": Book.objects.all()
    # select * from Blog
    }
    return render(request, 'full_stack_books/index.html', context)


def process(request):

    Book.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
    return redirect('/')
