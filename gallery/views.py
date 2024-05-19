from django.shortcuts import render ,redirect
from .models import Product 
from django.http import HttpResponse 
  
  
def product_list(request): 
    products = Product.objects.all() 
    return render(request, 'index.html', {'products': products}) 
  
  
def home(request): 
    return HttpResponse('Hello, World!') 

def input(request):
    if request.method=='POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image =request.FILES.get('image')
        product = Product(name=name, description=description, image=image)
        product.save()
        return redirect('product_list')
        
    return render(request,'input.html')