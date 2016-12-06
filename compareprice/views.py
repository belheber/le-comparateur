from django.shortcuts import render
from subprocess import Popen
from .forms import SerachForm

# Create your views here.


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
            pro =  pr.get_urls(product)[:20]
            context_dict = {'products':pro,'form':form}
            return render(request, 'bs.html', context_dict)
  else:
        form = SerachForm()
  pro =  pr.get_urls(product)[:6]
  context_dict = {'products':pro,'form':form}
  return render(request, 'bs.html', context_dict)
