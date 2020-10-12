from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('home', views.home_page, name='home_page'),
    path('news', views.news_page, name='news_page'),
    path('contact', views.contact_page, name='contact_page'),
    path('about', views.about_page, name='about_page'),
]