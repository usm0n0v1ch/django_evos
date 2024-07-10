from django.urls import path

from evos_app import views

urlpatterns = [
    path('control_panel/',views.control_panel,name='control_panel'),
    path('control_panel_categories/',views.control_panel_categories,name='control_panel_categories'),
    path('control_panel_foods/',views.control_panel_foods,name='control_panel_foods'),
    path('control_panel_users/',views.control_panel_users,name='control_panel_users'),
    path('menu/', views.menu,name='menu'),
    path('menu/category/<int:pk>/', views.menu_by_category, name='menu_by_category'),
    path('basket/', views.basket,name='basket'),
    path('profile/',views.profile,name='profile')
]