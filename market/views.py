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

class ProductListView(generic.ListView):
    model = Product
    #paginate_by = 10

class ProductDetailView(generic.DetailView):
    model = Product
    