#from __future__ import unicode_literals

from django.shortcuts import render
#from django.conf import settings
#from django.utils import timezone

from django.db.models import Q
from shopping_cart.models import Order
from market.models import Product, Seller, Category
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib import auth

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

def product_list(request):
    object_list = Product.objects.all()

    if 'search' in request.GET:
        search_item = request.GET['search']
        object_list = Product.objects.filter(name__icontains=search_item)
    '''
    queryset_list = Product.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Product.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(name__icontains=query)
    '''

    if request.user.is_authenticated:
        filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [product.product for product in user_order_items]

        context = {
            'product_list': object_list,
            'current_order_products': current_order_products,
        }

    else:
        context = {
            'product_list': object_list,
        }

    return render(request, "market/product_list.html", context)

class ProductDetailView(generic.DetailView):
    model = Product

class SellerListView(generic.ListView):
    model = Seller
    #paginate_by = 10

class SellerDetailView(generic.DetailView):
    model = Seller

def category_list(request):
    object_list = Category.objects.all()

    if 'search' in request.GET:
        search_item = request.GET['search']
        object_list = Category.objects.filter(name__icontains=search_item)

    context = {
            'category_list': object_list,
        }

    return render(request, "market/category_list.html", context)

class CategoryDetailView(generic.DetailView):
    model = Category



'''
def search(request):
    query = request.GET.get('q')
    results = Product.objects.filter(Q(name__icontains=query))
    object_list = Product.objects.all()
    #object_list = Product.objects.all()
    if request.user.is_authenticated:
        filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [product.product for product in user_order_items]

        context = {
            'product_list': object_list,
            'current_order_products': current_order_products,
        }

    else:
        context = {
            'product_list': results,
        }

    return render(request, "market/product_list.html", context)
'''
    