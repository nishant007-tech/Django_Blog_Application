from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logoutuser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('post/', views.post, name='post'),
    path('my_post/<int:id>/', views.my_post, name='my_post'),
    path('my_post/<int:id>/remove', views.post_remove, name='post_remove'),

]