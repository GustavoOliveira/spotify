from django.urls import path
from . import views

urlpatterns = [
    path('', views.MensagemList.as_view() ),
    path('<int:pk>', views.MensagemDetail.as_view())
]