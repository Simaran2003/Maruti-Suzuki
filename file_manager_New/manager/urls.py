from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    # path('C:',views.index, name='index'),
    path('<path:directory>/',views.list_folders, name='list_folders'),
    path('',views.index , name='index_1'),
    path('http://127.0.0.1:8000/D:/documents/ESPN/TIC/', views.list_folders, name='doc_list'),
    # path('<path:directory>/',views.list_subitems, name='list_subitems'),
    # path('<path:directory>/<str:filename>/',views.open_file, name='open_file'),
    # path('<str:directory>/',views.list_folders, name='list_folders'),

]