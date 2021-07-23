from django.urls import path
from store.views.home import Index
from store.views.signup import signup
from store.views.login import Login
from store.views.logout import logout
from store.views.cart import Cart
from store.views.ckeckout import CheckOut
from store.views.order import OrderView
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('signup', signup, name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='check'),
    path('order', auth_middleware(OrderView.as_view()), name='order'),
]