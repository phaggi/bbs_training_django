"""
#  low level render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Bd


def index(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bd.objects.order_by('-published')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))
"""
from django.shortcuts import render
from .models import Bd


def index(request):
    bbs = Bd.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs})
