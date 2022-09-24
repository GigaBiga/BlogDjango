from django.shortcuts import render
from django.http import HttpResponse

post =[
    {
        'author': 'Bro',
        'title': 'Something',
        'content':'First post',
        'date_posted': '24/8/2022'
    },
    {
        'author': 'Broette',
        'title': 'Something',
        'content':'First post',
        'date_posted': '25/8/2022'
    }
]


def home(request):
    context = {'posts': post}
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})