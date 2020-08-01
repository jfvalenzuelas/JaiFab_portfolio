from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_entries, name='all_entries'),
    path('<int:entry_id>/', views.detail, name='detail'),
]