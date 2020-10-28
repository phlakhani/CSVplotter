from django.urls import path
from .views import home, upload_file, resultview


urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload_file, name='upload_file'),
    path('upload/showresult', resultview, name='showresult')
   ]