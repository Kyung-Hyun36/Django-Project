from django.shortcuts import render
from third.models import Restaurant
from django.core.paginator import Paginator
from third.forms import RestaurantForm
from django.http import HttpResponseRedirect


# Create your views here.
def list(request):
    restaurants = Restaurant.objects.all()
    paginator = Paginator(restaurants, 5)

    page = request.GET.get('page')
    items = paginator.get_page(page)

    context = {
        'restaurants': items
    }
    return render(request, 'third/list.html', context)


def create(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/third/list/')
    form = RestaurantForm()
    return render(request, 'third/create.html', {'form': form})
