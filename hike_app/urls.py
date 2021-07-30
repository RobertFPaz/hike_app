from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('remove/<int:hike_id>', views.remove),
    path('new', views.new),
    path('join', views.join),
    path('join/<int:hike_id>', views.joinHike),
    path('logout', views.logout),
    path('delete/<int:hike_id>', views.delete),
    path('edit/<int:hike_id>', views.edit),
    path('details/<int:hike_id>', views.details),
    path('account', views.account),
]