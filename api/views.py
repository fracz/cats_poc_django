from django.shortcuts import render

from api.models import Cat


def cats_in_html(request):
    cats = Cat.objects.all()
    return render(request, 'api/cats-in-html.html', {'cats': cats})
