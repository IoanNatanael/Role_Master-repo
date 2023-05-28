from django.urls import path

from userextend import views
from userextend.views import error_view

urlpatterns = [
    path('create-user/', views.UserExtendCreateView.as_view(), name='create_user'),
    path('activate-user/<int:pk>/<str:token>/', views.activate_user, name='activate-user'),
    path('error/', error_view, name='error'),
]
