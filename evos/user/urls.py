from django.urls import path

from user import views

urlpatterns =[
    path('sign-up/', views.register_view,name='register_page'),
    path('', views.login_view, name='login_page'),
    path('logout/', views.logout_view, name='logout_page'),
]