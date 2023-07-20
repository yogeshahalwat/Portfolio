from django.urls import path
from . import views

app_name='blog'   # cretae the app name and then pass in html

urlpatterns = [
    path("",views.Blog,name="blog"),
    path("<int:pk>",views.detail,name="detail")


]