from django.urls import path
from . import views

app_name = 'list'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('others_list/', views.others_list, name='others_list'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/create_comment/', views.create_comment, name='create_comment'),
    path('<int:id>/delete_comment/<int:pk>', views.delete_comment, name='delete_comment'),
    path('<int:pk>/status_update/', views.status_update, name='status_update'),
    path('share_open/', views.share_open, name='share_open'),
    path('share_close/', views.share_close, name='share_close'),
]
