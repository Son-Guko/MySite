from django.urls import path
from . import views
from .views import upload_file

urlpatterns = [
    path('<int:id>',views.index, name='index'),
    path('',views.home, name='home'),
    path('create/', views.create, name='create'),
    path('upload/', upload_file, name='upload_file')
]