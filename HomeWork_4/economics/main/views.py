from django.shortcuts import render
from django.http import HttpResponseNotAllowed


def render_home(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        return HttpResponseNotAllowed(["GET"])
