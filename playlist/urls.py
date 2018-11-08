from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlayListList.as_view() ),
    path('<int:pk>', views.PlayListDetail.as_view())
]