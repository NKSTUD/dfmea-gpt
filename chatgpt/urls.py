from django.urls import path

from chatgpt import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prompt', views.prompt, name='prompt'),
    path('delete/<int:pk>', views.delete_table, name='delete_table'),
]
