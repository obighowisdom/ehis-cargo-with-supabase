from django.urls import path
from . import views

app_name = 'myappurl'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('track/', views.track, name = 'track'),
    path('result/', views.result, name = 'result'),
    path('loc_two/', views.details_two, name = 'loc_two'),
    path('test/', views.test, name = 'test'),

]