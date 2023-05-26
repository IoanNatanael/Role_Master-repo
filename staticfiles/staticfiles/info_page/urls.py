from django.urls import path
from info_page import views

# app_name = 'info_page'

urlpatterns = [
    path('info-page/', views.InfoTemplateView.as_view(), name='info_page'),
    path('info-post-list/', views.info_post_list, name='info_post_list'),
    path('info-post-create/', views.info_post_create, name='info_post_create'),
    path('info-post-delete/<int:post_id>/', views.info_post_delete, name='info_post_delete'),
    path('info-post-edit/<int:post_id>/', views.info_post_edit, name='info_post_edit'),
]
