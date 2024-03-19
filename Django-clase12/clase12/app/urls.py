from django.urls import path
from .views import estudiante

urlpatterns = [
    path('', estudiante , name="estudiante" )
]