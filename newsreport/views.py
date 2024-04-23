from django.shortcuts import render
import requests

# Create your views here.
def newspaper(request):
    return render(request,"news.html")

def sportspage(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=sports")
    response =url.json()
    sportsnews = response["data"]
    context = {
        "sportsnews":sportsnews
    }
    return render(request,"sports.html",context)

def politics(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=politics")
    response = url.json()
    politicspage = response["data"]
    context = {
        "politicspage":politicspage
    }
    return render(request,"politics.html",context)

def indexpage(request):
    return render(request,"index.html")

def nationalpage(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=national")
    response = url.json()
    national = response["data"]
    context = {
        "national":national
    }
    return render(request,"national.html",context)