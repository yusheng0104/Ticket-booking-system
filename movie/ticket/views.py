from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from ticket.forms import RegistrationForm
import stripe

from .models import Cinima, Movies, Coupon

cinimas = []
movienames = []
prices = []
total = []

stripe.api_key = 'sk_test_ubAQED9Kk0zAw6MR4HGibjbO00ihpb4iSB'

def index(request):
    if not request.user.is_authenticated:
        form = RegistrationForm()
        return render(request, 'ticket/register.html', {'form': form})
    context = {
        "user": request.user
    }
    return render(request, "ticket/user.html", context)

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "ticket/login.html", {"message": "Please Login"})
        else:
            return HttpResponse("Invalid Form!!")

    else:
        form = RegistrationForm()
        return render(request, 'ticket/register.html', {'form': form})

def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        cinimas = Cinima.objects.all()
        context = {
            "cinimas": cinimas,
        }
        return render(request, "ticket/user.html", context)
    else:
        return render(request, "ticket/login.html", {"message": "Invalid credentials."})

def cinima(request, cinima_id):
    cinimas.clear()
    try:
        cinima = Cinima.objects.get(pk=cinima_id)
        movies = Movies.objects.all()
        cinimas.append(cinima)
    except Cinima.DoesNotExist:
        raise Http404("Cinima does not exist")
    context = {
        "cinimas": cinimas,
        "movies": movies,
    }
    return render(request, "ticket/cinima.html", context)

def movielist(request):
    movieforselect = Movies.objects.all()
    context = {
        "cinimas": cinimas,
        "movies": movieforselect
    }
    return render(request, "ticket/cinima.html", context)

def addtocart(request, movie_id):
    total.clear()
    movie = Movies.objects.get(pk=movie_id)
    movieprice = float(movie.price)
    movienames.append(movie.name)
    prices.append(movieprice)
    total.append(sum(prices))
    context = {
        "cinimas": cinimas,
        "prices": prices,
        "movienames": movienames,
        "total":total,
    }
    return render(request, "ticket/cart.html", context)

def coupon(request):
    total.clear()
    value=0
    coupon_name = request.POST.get("coupon")
    coupon = Coupon.objects.all()
    for c in coupon:
        if c.name == coupon_name:
            value = c.value
    total.append(sum(prices)-float(value))
    context = {
        "cinimas": cinimas,
        "prices": prices,
        "movienames": movienames,
        "total":total,
    }
    return render(request, "ticket/cart.html", context)

def checkout(request):
    username = request.user.username
    email = request.user.email
    context = {
        "total": total,
        "message": "Your order has been placed"
    }
    send_mail('Order placed', 'Dear ' + username+': Your order has been placed. You paid $'+str(total[0])+", and your cinima is "+ str(cinimas[0]), settings.EMAIL_HOST_USER,
              [email], fail_silently=False)
    movienames.clear()
    prices.clear()
    charge = stripe.Charge.create(
        amount=100*int(total[0]),
        currency='usd',
        description='Example charge',
        source='tok_visa',
    )
    return render(request, "ticket/checkout.html", context)

def logout_view(request):
    logout(request)
    return render(request, "ticket/login.html", {"message": "Logged out."})
