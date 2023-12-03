from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_page,name='login_page'),
    path('register/',views.register_page,name='register_page'),
    path('logout/',views.logout_page,name='logout_page'),
    
    path('home/list/', views.getlist),
    path('home/', views.gethome, name='home'),
    path('submit/', views.post, name='submit'),
    path('home/sell/', views.display),
    path('home/recommend', views.get_recommendation),
    path('home/recommend/result', views.get_crop_result, name='result'),
    path('home/predict', views.get_prediction),
    path('home/predict/answer', views.cnn_fertilizer, name='ans'),
    path('home/mandi', views.live, name="mandi"),
    
]
