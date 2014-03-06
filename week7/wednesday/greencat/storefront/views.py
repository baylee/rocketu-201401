from django.http import HttpResponse, Http404
from django.shortcuts import render
from storefront.models import Category


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def support(request):
    return HttpResponse("Support")


def shop(request):
    return HttpResponse("Shop")


def category(request, category):
    try:
        category = Category.objects.get(name=category)
    except Category.DoesNotExist:
        raise Http404

    products = category.product_set.all()

    data = {"category": category, "products": products}
    return render(request, "category.html", data)


def product_detail(request, product_name):
    return HttpResponse("Product Detail {0}".format(product_name))