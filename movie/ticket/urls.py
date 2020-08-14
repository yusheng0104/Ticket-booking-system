from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
    path("<int:cinima_id>", views.cinima, name="cinima"),
    path("logout", views.logout_view, name="logout"),
    path("<int:movie_id>/addtocart", views.addtocart, name="addtocart"),
    path("movielist", views.movielist, name="movielist"),
    path("checkout", views.checkout, name="checkout"),
    path("coupon", views.coupon, name="coupon"),
]
