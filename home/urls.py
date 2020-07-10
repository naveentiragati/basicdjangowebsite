#from django.contrib import admin
#from django.urls import path, inculde 

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('home/', include('home.urls'))
#]

from django.contrib import admin
from django.urls import path, include 
from home import views

urlpatterns = [
    
    path('about/', views.home, name= 'abt')
]