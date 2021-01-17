from django.contrib import admin
from django.urls import path, include
from shop import views as shop_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', shop_views.Categories.as_view()),
    path('category/<str:category>/', shop_views.Products.as_view()),
    path('product/<int:product_id>/', shop_views.ProductsDetails.as_view()),
    path('order/create/', shop_views.MakeOrder.as_view()),
    path('products/new/', shop_views.NewProducts.as_view()),
    path('images/<str:filename>', shop_views.ImageView.as_view()),
    #auth
    path('account/', include('authSystem.urls')),
    path('cart/', include('shopping_cart.urls')),
]
