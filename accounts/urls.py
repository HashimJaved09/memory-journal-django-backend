from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('api/user/create', views.UserCreate.as_view(), name='account-create'),
    path('api/users', views.UsersView.as_view(), name='users-view'),
    path('api/edit/<int:pk>/user', views.UserEditView.as_view(), name='users-view'),

]