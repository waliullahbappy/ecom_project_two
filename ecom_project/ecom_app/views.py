
from django.shortcuts import render
from ecom_app.models import Setting
from product_app.models import Products,Images


# Create your views here.

def home(request):
    setting = Setting.objects.get(id=1)
    slider_image = Products.objects.all().order_by('id')[:3]
    latest_product = Products.objects.all().order_by('-id')
    featured_product = Products.objects.all()
    
    context={
        'setting':setting,
        'slider_image':slider_image,
        'latest_product':latest_product,
        'featured_product':featured_product,
        }
    return render(request, 'home.html',context)
    
def single_product(request,id):
    setting = Setting.objects.get(id=1)
    single_product = Products.objects.get(id=id)
    small_images = Images.objects.filter(product_id=id)
    same_category_img = Products.objects.all().order_by('id')[:5]

    context ={
        'setting':setting,
        'single_product':single_product,
        'small_images':small_images,
        'same_category_img':same_category_img
        
    }
    return render(request, 'single_product.html',context)