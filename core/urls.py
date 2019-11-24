from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('api/memories', views.MemoryView.as_view(), name='memories'),
    path('api/memory/<int:pk>', views.MemoryEditView.as_view(), name='users-view'),

]