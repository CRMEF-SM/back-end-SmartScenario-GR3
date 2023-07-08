from .views import ActivitiesCreateView,ActivitiesListView,ActivityDeteteView,OneActivityDetailView,UpdateActivityView,ActivitySearchbynameAPIView

from django.urls import path

urlpatterns = [
    path('create/', ActivitiesCreateView.as_view(), name='activities-create'),
    path('get/', ActivitiesListView.as_view(), name='all-activities'),
    path('delete/<int:pk>/', ActivityDeteteView.as_view(), name='delete-activities'),
    path('edit/<int:pk>/', OneActivityDetailView.as_view(), name='edit-activities'),
    path('update/<int:pk>/', UpdateActivityView.as_view(), name='updates-activities'),
    path('api/activities/', ActivitySearchbynameAPIView.as_view(), name='activity-search-name'),
]