from django.shortcuts import render
from django.http import HttpResponse
from contextvars import Context
from multiprocessing import context


def azzani(request):
    return HttpResponse('<h1>Azzani First Blog</h1>')


def janeen(request):
    return HttpResponse('<h1> Janeen is my love</h1>')    
