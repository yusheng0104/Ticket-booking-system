# Movie ticket booking system
In the project, I designed an app for movie ticket.
The users could register, and login the app to select a cinema and purchase movie tickets.(Pardon my typo on cinema, I run out of time to fix it)
A coupon could be applied, and credit card will be charged and an email will be sent to the user after pressing pay button.
1. cart.html, a page handling cart with selected movies. The cinema name will be shown in the page.
2. checkout.html, a page give information about successful Checkout.
3. cinima.html, a page showing movie list to a certain cinema.
4. login.html, login page.
5. register.html, register page.
6. user.html, showing cinema list to certain user.
7. models.py, three forms including cinima, movie and coupon.
8. settings.py, was revised to handle send_mail.
9. views.py, a list functions are included. As following: register_view, login_view, logout, coupon, movielist, addtocart, checkout, and cinima.
10. stripe test function was used to handle credit card.
11. mobile-responsive was fulfilled by color change when the page size changed.
12. Python, sqlite, and JavaScript were used in this application.
