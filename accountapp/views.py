from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hi_nini(request):
    if request.method == "POST":
        return render(request, 'accountapp/hi_nini.html',
                      context={'text':'POST METHOD'})
    else:
        return render(request, 'accountapp/hi_nini.html',
                      context={'text':'GET METHOD'})

