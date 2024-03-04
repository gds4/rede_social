from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('post/new', views.new_post, name ='new_post'),
    path('post/<int:id>', views.detail_post, name = 'detail_post'),
    path('perfil/<str:nickname>', views.perfil, name='perfil')
]