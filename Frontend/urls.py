from django.urls import path
from Frontend import views

urlpatterns=[
    path('homepage/',views.homepage, name="homepage"),
    path('product_page/<cname>/',views.product_page, name="product_page"),
    path('aboutpage/',views.aboutpage, name="aboutpage"),
    path('contactpage/',views.contactpage, name="contactpage"),
    path('singleproduct/<int:proid>/',views.singleproduct, name="singleproduct"),
    path('contactsave/',views.contactsave, name="contactsave"),
    path('userlogin/',views.userlogin, name="userlogin"),
    path('reg_save/',views.reg_save, name="reg_save"),
    path('signup_page/',views.signup_page, name="signup_page"),
    path('Userlogout/',views.Userlogout, name="Userlogout"),
    path('cart_save/',views.cart_save, name="cart_save"),
    path('cartpage/',views.cartpage, name="cartpage"),
    path('cartdelete/<p_id>',views.cartdelete, name="cartdelete"),
    path('checkoutpage/',views.checkoutpage, name="checkoutpage"),
    path('save_checkout/',views.save_checkout, name="save_checkout"),
]