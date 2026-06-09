from django.urls import path, include
from . import views 
from rest_framework.routers import DefaultRouter
from .views import *
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'items', ItemView)

urlpatterns=[
    path('api/admin/', include(router.urls)),
    path('adminpanel', views.admin_panel_page),
    path('shop', views.shop_page),
    path('login', views.login_page),
    path('signup', views.signup_page),
    path('header', views.header_page),
    path('home', views.home_page),
    path('about', views.about_page),
    path('footer', views.footer_page),
    path('shop/checkout', views.checkout_page),
    path('history', views.history_page),
    path('forbidden', views.forbidden_430_view, name='forbidden'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])