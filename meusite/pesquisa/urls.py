from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:questao_id>/', views.detalhe, name='detalhe'),
    path('<int:questao_id>/resultado/', views.resultado, name='resultado'),
    path('<int:questao_id>/votacao/', views.votacao, name='votacao'),
]