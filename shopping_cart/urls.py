from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.CartItemCreateView.as_view()),
    # path('delete-item/', views.DeleteItemFromCart.as_view()),
    # path('clear-cart/', views.ClearCart.as_view()),
]
