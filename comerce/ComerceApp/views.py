import requests
from django.shortcuts import render
from requests.compat import quote_plus
from bs4 import BeautifulSoup
from . import models

KUFAR_BASE_URL= 'https://www.kufar.by/listings?query={}&ot=1&rgn=&ar='
KUFAR_BASE_IMG_URL= 'https://yams.kufar.by/api/v1/kufar-ads/images/{}.jpg?rule=line_thumbs'

def home_page(request):
    return render(request, template_name='base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search = search)
    final_url = KUFAR_BASE_URL.format(quote_plus(search))
    responce = requests.get(final_url)
    data=responce.text
    soup= BeautifulSoup(data, features='html.parser')

    post_block = soup.find_all('a', {'class': 'k-eoCs-37aaa'})

    final_postings=[]
   
    for post in post_block:
        post_title = post.find(class_='k-eoGq-d16af').text  
        post_url = post.get('href')
        post_price = post.find(class_='k-ejrZ-a3c0f').text
        post_img = post.find(class_='k-eoGQ-a6fd3').get('data-src')

        # if post.find(class_='k-ejrZ-a3c0f'):
        #     post_price = post.find(class_='k-ejrZ-a3c0f').text
        # elif (post.find(class_='k-ejrZ-a3c0f').text == "Договорная"):
        #     post_price = "На капоте"
            

    
        final_postings.append((post_title, post_url, post_price, post_img))
        print()

    
    stuff_for_frontend = {
        'search' : search,
        'final_postings' : final_postings,
        }
    return render(request, template_name='ComerceApp/new_search.html', context=stuff_for_frontend)
    