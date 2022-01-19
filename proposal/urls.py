from django.urls import path
from . import views

urlpatterns = [
    path('proposta/<int:id>/', views.proposta, name='proposta'),
]