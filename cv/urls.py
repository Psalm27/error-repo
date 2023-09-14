from django.urls import path
from .views import upload_docs, list_cvs, list_cover

app_name = 'cv'
urlpatterns = [

    path('add/', upload_docs, name='upload_docs'),
    path('cvs/', list_cvs, name='user_cvs'),
    path('coverletter/', list_cover, name='user_coverletter'),

]
