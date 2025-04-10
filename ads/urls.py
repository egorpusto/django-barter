from django.urls import path
from . import views

urlpatterns = [
    path('', views.ad_list, name='ad_list'),
    path('create/', views.ad_create, name='ad_create'),
    path('<int:pk>/edit/', views.ad_edit, name='ad_edit'),
    path('<int:pk>/delete/', views.ad_delete, name='ad_delete'),
    # Обмен предложениями
    path('proposals/', views.proposal_list, name='proposal_list'),
    path('proposals/create/', views.create_proposal, name='create_proposal'),
    path('proposals/<int:pk>/<str:status>/', views.update_proposal_status, name='update_proposal_status'),

]
