from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    """Returns Hello World"""
    return render(request, 'hello.html', {'name': 'Bamidele'})
    # return HttpResponse('Hello World')
