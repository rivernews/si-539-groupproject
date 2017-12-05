from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'GET':
        vars = {}
        return render(request,'index2.html',vars)