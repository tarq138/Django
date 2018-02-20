from django.shortcuts import render
from .forms import SubscribersForm
from products.models import *


def index(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    form = SubscribersForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        print(data["name"])
        new_form = form.save()

    return render(request, 'mainApp/homePage.html', locals())
