final-project
In the project, I designed an app for movie ticket. The users could register, and login the app to select a cinema and purchase movie tickets.(Pardon my typo on cinema, I run out of time to fix it) A coupon could be applied, and credit card will be charged and an email will be sent to the user after pressing pay button.

cart.html, a page handling cart with selected movies. The cinema name will be shown in the page.
checkout.html, a page give information about successful Checkout.
cinima.html, a page showing movie list to a certain cinema.
login.html, login page.
register.html, register page.
user.html, showing cinema list to certain user.
models.py, three forms including cinima, movie and coupon.
settings.py, was revised to handle send_mail.
views.py, a list functions are included. As following: register_view, login_view, logout, coupon, movielist, addtocart, checkout, and cinima.
stripe test function was used to handle credit card.
mobile-responsive was fulfilled by color change when the page size changed.
Python, sqlite, and JavaScript were used in this application.
