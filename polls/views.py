from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("수진이는 궁디 만지작.")
