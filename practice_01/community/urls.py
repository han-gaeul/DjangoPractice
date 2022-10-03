from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
  path('', views.index, name='index'),
  path('detail/<int:pk>',views.detail, name='detail'),
  path('new/', views.new, name='new'),
  path('edit/<int:pk>', views.edit, name='edit'),
  path('create/', views.create, name='create'),
  path('update/<int:pk>', views.update, name='update'),
  path('delete/<int:pk>', views.delete, name='delete'),
]