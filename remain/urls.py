from django.urls import path
from .views import home_page,dlt_task
urlpatterns = [
    path('',home_page,name='index'),
    path('dlt/<int:pk>/',dlt_task,name='dlt')
]


app_name='remain'