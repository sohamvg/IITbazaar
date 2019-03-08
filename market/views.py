from django.shortcuts import render
from market.models import Product, Seller, Category

# Create your views here.

def index(request):
    num_products = Product.objects.all().count()
    num_sellers = Seller.objects.all().count()
    num_categories = Category.objects.all().count()

    context = {
        'num_products': num_products,
        'num_sellers': num_sellers,
        'num_categories': num_categories,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic
'''
class ProductListView(generic.ListView):
    model = Product
    #paginate_by = 10
'''
def product_list(request):
    all_products = Product.objects.all()
    context = {
        'all_products':all_products
    }
    return render(request,'market/products.html',context=context)

class ProductDetailView(generic.DetailView):
    model = Product

class SellerListView(generic.ListView):
    model = Seller
    #paginate_by = 10

class SellerDetailView(generic.DetailView):
    model = Seller
    