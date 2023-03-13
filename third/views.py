from django.shortcuts import render
from third.models import Restaurant
from django.core.paginator import Paginator


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
