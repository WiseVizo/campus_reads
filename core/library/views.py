from django.shortcuts import render
from django.http.response import HttpResponse
from django.conf import settings

# Create your views here.
def home_page(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, "library/index.html", context=context)