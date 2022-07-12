from django.shortcuts import render
from .models import HomeCarusel, HomeCategory, HomeSubCategory, HomeFeatureItem, HomeBrand, HomeRec
from django.views.generic import ListView, DetailView
# Create your views here.


class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homecarusels = HomeCarusel.objects.all()
        category = HomeCategory.objects.all()
        brands = HomeBrand.objects.all()
        items = HomeFeatureItem.objects.all()
        recs = HomeRec.objects.all()
        return render(request, self.template_name, {'homecarusels':homecarusels, 'category':category, 'brands':brands, 'items':items, 'recs':recs})

