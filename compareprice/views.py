from django.shortcuts import render

from .forms import SerachForm

# Create your views here.

from pkgs.webscrap import scrap as sc
from pkgs.webscrap import scraper as scr



def get_name(request):
    product = ''
    scr.link_scrap()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SerachForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            product = form.cleaned_data['search']
            price = sc.get_urls(product)
            price_avi = price[:5]

            return render(request, 'compareprice/page.html', {'data': price_avi, 'scr_title':"anything"})

            # if a GET (or any other method) we'll create a blank form
    else:
        form = SerachForm()
    price = sc.get_urls(product)
    price_avi = price[:5]
    
    return render(request, 'compareprice/page.html', {'data': price_avi, 'scr_title':"anything"})
