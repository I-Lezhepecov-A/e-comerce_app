from django.shortcuts import render

def home_page(request):
    return render(request, template_name='base.html')

def new_search(request):
    search = request.POST.get('search')
    stuff_for_frontend = {
        'search':search,
        }
    return render(request, template_name='ComerceApp/new_search.html', context=stuff_for_frontend)