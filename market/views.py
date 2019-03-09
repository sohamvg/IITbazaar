from __future__ import unicode_literals

from django.shortcuts import render

from shopping_cart.models import Order
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

def product_list(request):
    object_list = Product.objects.all()
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
    	user_order = filtered_orders[0]
    	user_order_items = user_order.items.all()
    	current_order_products = [product.product for product in user_order_items]

    context = {
        'product_list': object_list,
        'current_order_products': current_order_products
    }

    return render(request, "market/product_list.html", context)

class ProductDetailView(generic.DetailView):
    model = Product

class SellerListView(generic.ListView):
    model = Seller
    #paginate_by = 10

class SellerDetailView(generic.DetailView):
    model = Seller
    