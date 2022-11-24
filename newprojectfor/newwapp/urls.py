from django.urls import path

from newwapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('reg_ster/',views.register,name='reg_ster'),
    path('log_in/',views.login,name='log_in'),
    path('logout/',views.logout,name='logout'),
    ]