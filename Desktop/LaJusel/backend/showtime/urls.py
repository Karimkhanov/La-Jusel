from django.urls import path
from .views import show_list, show_add, get_show_detail

urlpatterns = [
    path('showtime', show_list),
    path('showtime/add/', show_add),
    path('showtime/<int:pk>/', get_show_detail)
]
