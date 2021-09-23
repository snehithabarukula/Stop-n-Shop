"""Onlineshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views,models
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('signUp/',views.signUp,name='signUp'),
	path('signIn/',auth_views.LoginView.as_view(template_name="shop/signIn.html"),name='signIn'),
	path('signOut/',auth_views.LogoutView.as_view(template_name="shop/header.html"),name='signOut'),
	path('main/',views.main,name='main'),
	path('usvw/',views.usvwe,name="usv"),
	#path('elevw/',views.elevw,name="elevw"),
    #path('elevw1/',views.elevw1,name="elevw1"),
    path('addtocart/<int:id>',views.addtocart,name='addtocart'),
    path('mycart/',views.mycart,name='mycart'),

	path('cloth/',views.cloth,name="cloth"),
	path('foot/',views.foot,name="foot"),
	path('kids/',views.kids,name="kids"),
	path('jew/',views.jew,name="jew"),
	path('sports/',views.sports,name="sports"),
	#path('dec/',views.dec,name="dec"),
	#path('clean/',views.clean,name="clean"),
	#path('books/',views.books,name="books"),
	path('la/',views.la,name="la"),
	path('trends/',views.trends,name="trends"),
	path('bs/',views.bs,name="bs"),
	path('tb/',views.tb,name="tb"),
	path('cloth1/',views.cloth1,name="cloth1"),
	path('foot1/',views.foot1,name="foot1"),
	path('kids1/',views.kids1,name="kids1"),
	path('jew1/',views.jew1,name="jew1"),
	path('sports1/',views.sports1,name="sports1"),
	#path('dec1/',views.dec1,name="dec1"),
	#path('clean1/',views.clean1,name="clean1"),
	#path('books1/',views.books1,name="books1"),
	path('la1/',views.la1,name="la1"),
	path('trends1/',views.trends1,name="trends1"),
	path('bs1/',views.bs1,name="bs1"),
	path('tb1/',views.tb1,name="tb1"),
	path('msg/',views.msg,name="msg"),
	path('remove/<int:kl>/',views.remove,name='remove'),
	path('purchase/',views.purchase,name="purchase"),
	path('checkout/',views.checkout,name='checkout'),

	path('profile/',views.profile,name='profile'),
	path('search/',views.search,name='search'),
	path('search1/',views.search1,name='search1'),
	path('edit/<int:pl>/',views.edit,name="edit"),
	
	
	

	

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)