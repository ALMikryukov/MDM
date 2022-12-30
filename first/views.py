import json
from django.dispatch.dispatcher import receiver
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import conf
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .models import *
from django.http import JsonResponse

# from .forms import *
# from .utils import *




def mainPage(request):

    parts = PartItem.objects.all()[:5]
    brands =  CarBrands.objects.all().order_by('name', )
    context = { 'parts': parts, 'brands':brands }

    return render(request, 'base.html', context)

def model(request, id) :
    models = CarModels.objects.all()
    brands = CarBrands.objects.all().order_by( 'name',)
    model = CarModels.objects.get(id=id)
    parts=  PartItem.objects.all()
    apps =   parts.filter(app=model)
    cats = Catalog.objects.all()
    categoryes = set()

    for z  in model.partitem_set.all():
        categoryes.add(z.category)

    search_query =''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    apps = apps.filter(Q(name__icontains=search_query) | Q(oem__icontains=search_query)
                       | Q(category__category__icontains=search_query))


    page = request.GET.get('page')
    results = 10
    paginator = Paginator(apps, results)

    try:
        apps  = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        apps = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        apps = paginator.page(page)



    context = {'model': model, 'apps':apps, 'cats': cats ,
               'models':models, 'brands': brands, 'categoryes':categoryes, 'paginator':paginator, 'results': results }
    print(search_query)
    return render(request, 'model.html', context )



def brand(request, id):
    brand = CarBrands.objects.get(id=id)
    models = brand.models.all()
    context = {'brand':brand, 'models':models}

    return render(request,  'models.html', context)


def oem(request, id):
    oem_ = PartItem.objects.get(id=id)
    oem_.app.all()

    # CarBrands.objects.get()
    context = {'oem_':oem_, }

    return render(request, 'oem.html', context)

def test_get_func(request, id):
    
    # model = CarModels.objects.get(id=id)
    parts =  PartItem.objects.get(id=id)
    # apps =   parts.filter(app=model)

    context = {'model': parts.toJSON()}

    return JsonResponse(context)

def test_func(request, id):
    models = CarModels.objects.all()
    brands = CarBrands.objects.all().order_by( 'name',)
    model = CarModels.objects.get(id=id)
    parts=  PartItem.objects.all()
    apps =   parts.filter(app=model)
    cats = Catalog.objects.all()
    categoryes = set()

    for z  in model.partitem_set.all():
        categoryes.add(z.category)

    search_query =''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    apps = apps.filter(Q(name__icontains=search_query) | Q(oem__icontains=search_query)
                       | Q(category__category__icontains=search_query))


    page = request.GET.get('page')
    results = 10
    paginator = Paginator(apps, results)

    try:
        apps  = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        apps = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        apps = paginator.page(page)



    context = {'model': model, 'apps':apps, 'cats': cats ,
               'models':models, 'brands': brands, 'categoryes':categoryes, 'paginator':paginator, 'results': results }
    print(search_query)


    return render(request,  'test_.html', context )






def basket(request):
    return render(request ,  'basket.html')

def about(request):
    return render(request ,  'aboutTheCompany.html')

def contacts(request):
    return render(request ,  'contacts.html')

def test(request):
    return render(request ,  'test.html')