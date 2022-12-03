from django.urls import path

from . import views

urlpatterns = [
    path('', views.function_one, name='function_one'),

]
