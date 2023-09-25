from django.shortcuts import render
from django.views.generic import View
from .models import *
# Create your views here.
class BaseView(View):
    views = {}
    views['categories'] = Category.objects.all()
    views['brands'] = Brand.objects.all()
    views['siteinfos'] = SiteInfo.objects.all()

class HomeView(BaseView):
    def get(self,request):
        self.views
        self.views['sliders'] = Slider.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['hots'] = Product.objects.filter(labels = 'hot')
        self.views['news'] = Product.objects.filter(labels='new')
        self.views['sales'] = Product.objects.filter(labels='sale')
        return render(request,'index.html',self.views)

class CategoryView(BaseView):
    def get(self,request,slug):
        self.views
        cat_id = Category.objects.get(slug = slug).id
        self.views['cat_products'] = Product.objects.filter(category_id = cat_id)
        return render(request,'Caategory.html',self.views)

class BrandView(BaseView):
    def get(self,request,slug):
        self.views
        br_id = Brand.objects.get(slug = slug).id
        self.views['brand_products'] = Product.objects.filter(brand_id = br_id)
        return render(request,'brand.html',self.views)

class DetailView(BaseView):
    def get(self,request,slug):
        self.views