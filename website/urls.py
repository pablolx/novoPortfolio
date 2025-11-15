from django.urls import path
from .views import ProjetosListView, ProjetosCreateView, ProjetosUpdateView, ProjetosDeleteView, index, contato

urlpatterns = [
    path('', index, name='home'),
    path('home/', index, name='home'),    
    path('projetos/', ProjetosListView.as_view(), name='projetos_list'),
    path('projetos/novo/', ProjetosCreateView.as_view(), name='projetos_create'),
    path('contato/', contato, name='contato'),
    path('update/<int:pk>/', ProjetosUpdateView.as_view(), name='projetos_update'),
    path('delete/<int:pk>/', ProjetosDeleteView.as_view(), name='projetos_delete'),
]