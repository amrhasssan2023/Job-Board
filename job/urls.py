from django.urls import path, include
from . import views 
urlpatterns = [
    path('',views.job_list,name='job_list'),
    path('add',views.add_job,name='add_job'),
    path('<str:slug>',views.job_details,name='job_details'),


    #__________________________________________
    path('api-auth/', include('rest_framework.urls'))
]