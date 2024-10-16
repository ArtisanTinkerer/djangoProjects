from django.urls import path
from . import views

app_name = 'raptor'
urlpatterns = [
    # sighting views
    path('', views.sighting_list, name='sightings_list'),
    path('<int:id>/', views.sighting_detail, name='sighting_detail')
]


