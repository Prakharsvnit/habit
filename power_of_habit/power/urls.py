from django.urls import path
from .views import HomeView
from .views import EditView

urlpatterns = [
	path('', HomeView.as_view(),name='home'),
	path('edit/',EditView.as_view(),name='edit'),
]