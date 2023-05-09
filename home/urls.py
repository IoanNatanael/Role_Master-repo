from django.urls import path
from home import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='homepage'),
    path('post-list/', views.post_list, name='post_list'),
    path('post-create/', views.post_create, name='post_create'),
    path('post-delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('post-edit/<int:post_id>/', views.post_edit, name='post_edit'),
]

