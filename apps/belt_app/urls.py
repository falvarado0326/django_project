from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),    
    url(r'^books$', views.books),    
    url(r'^users/(?P<id>\d+)$', views.user),
    url(r'^books/add$', views.add_book),     
    url(r'^books/(?P<id>\d+)$', views.reviews),
    url(r'^login$', views.login)   
]