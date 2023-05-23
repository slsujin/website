from .import views
from django.urls import path

urlpatterns = [
    path('', views.web1,name='web1'),

]