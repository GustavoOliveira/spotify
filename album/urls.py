from django.conf.urls import url
from . import views
from .views import AlbumList
from django.urls import path

urlpatterns = [
    path('', views.AlbumList.as_view(), name='file-upload'),  
    #url(r'^upload/$', AlbumList.as_view(), name='file-upload'),
    path('<int:pk>', views.AlbumDetail.as_view()),
]