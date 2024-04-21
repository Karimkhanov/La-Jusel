from django.urls import path

from .views import MenuView, MenuDetailView

urlpatterns = [
    path('menu/', MenuView.as_view()),
    path('menu/<int:pk>/', MenuDetailView.as_view()),

]
