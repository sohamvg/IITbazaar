from django.urls import path
from . import views
from django.conf.urls import url
from .views import product_list, category_list

app_name = 'market'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', product_list, name='products'),
    #path('results/', search, name='search'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('categories/', category_list, name='categories'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('sellers/', views.SellerListView.as_view(), name='sellers'),
    path('seller/<int:pk>', views.SellerDetailView.as_view(), name='seller-detail'),
]