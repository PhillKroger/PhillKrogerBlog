from django.shortcuts import render

# Create your views here.
def mainapp(request):
    return render(request, "mainapp/index.html")