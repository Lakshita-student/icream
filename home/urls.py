from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Product/', views.Product, name='Product'),
    path('product_detail/', views.product_detail, name='product_detail'),
    path('About/', views.About, name='About'),
    path('Blog/', views.Blog, name='Blog'),
    path('Blog_detail/', views.Blog_detail, name='Blog_detail'),
    path('Cart/', views.Cart, name='Cart'),
    path('Checkout/', views.Checkout, name='Checkout'),
    path('Contact/', views.Contact, name='Contact'),
    path('Gallery/', views.Gallery, name='Gallery'),
    path('Wishlist/', views.Wishlist, name='Wishlist'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

