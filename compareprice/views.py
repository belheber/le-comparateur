from django.shortcuts import render
from subprocess import Popen
from .forms import SerachForm

# Create your views here.

#from pkgs.webscrap import scrap as sc
#from pkgs.webscrap import all
<<<<<<< HEAD
#pyth_exec = './pkgs/webscrap/scraper.py'
#Popen(["python",pyth_exec], close_fds=True)
=======
pyth_exec = '/app/pkgs/webscrap/scraper.py'
Popen(["python",pyth_exec], close_fds=True)
>>>>>>> e050e4596b33d110b3a6ff7e18de2a40adfd2a19

from pkgs import get_products as pr

def index(request):
  product = ''
  if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SerachForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            product = form.cleaned_data['search']
            pro =  pr.get_urls(product)[:6]
            context_dict = {'products':pro,'form':form}
            return render(request, 'bs.html', context_dict)
  else:
        form = SerachForm()
  pro =  pr.get_urls(product)[:6]
  context_dict = {'products':pro,'form':form}
  return render(request, 'bs.html', context_dict)


'''
def get_name(request):
    product = 'villa'
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

            return render(request, 'compareprice/name.html', {'form':form, 'data': price_avi, 'scr_title':"anything"})

            # if a GET (or any other method) we'll create a blank form
    else:
        form = SerachForm()
    price = sc.get_urls(product)
    price_avi = price[:5]
    
    return render(request, 'compareprice/name.html', {'form':form,'data': price_avi, 'scr_title':"anything"})
'''
