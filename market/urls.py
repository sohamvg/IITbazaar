from django.urls import path
from . import views

app_name = 'market'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('sellers/', views.SellerListView.as_view(), name='sellers'),
    path('seller/<int:pk>', views.SellerDetailView.as_view(), name='seller-detail'),
]