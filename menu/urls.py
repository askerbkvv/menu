from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='home'),
    path('catery/<str:data>', views.category_page, name='category'),
]

