from django.urls import path

from characters import views

app_name = 'characters'

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list'),
    path('add/', views.CharacterCreateView.as_view(), name='character_create'),
    path('<slug:slug>/', views.CharacterDetailView.as_view(), name='character_detail'),
    path('<slug:slug>/edit/', views.CharacterUpdateView.as_view(), name='character_update'),
    path('<slug:slug>/delete/', views.CharacterDeleteView.as_view(), name='character_delete')
]