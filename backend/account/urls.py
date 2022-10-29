from django import views
from django.urls import path
from .views import( MyTokenObtainPairView,UserCreateView,UserCreate,
ApplicationCreateView,ApplicationListView,ApplicationDetailView,UserListView,
approveRequest,declineRequest,seat,userBlockView,AprovedApplicationView,DeniedApplicationView,AllotedSeat,ClearSeat
)
from rest_framework_simplejwt.views import (
  
    TokenRefreshView,
)
from . import views 
urlpatterns = [
    
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.UserCreate ,name='user-create'),
    path('userlist/', UserListView.as_view() ,name='user-list'),
    path('userlist/block/<int:id>/', userBlockView.as_view() ,name='user-block'),

    path('create/', ApplicationCreateView.as_view(), name='apllication-create'),
    path('application_list/', ApplicationListView.as_view(), name='apllication-list'),
    path('application_list/<int:pk>/', ApplicationDetailView.as_view(), name='apllication-detail'),
    path('application_list/approved/<int:pk>/', approveRequest.as_view(), name='request-aproved'),
    path('application_list/declined/<int:pk>/', declineRequest.as_view(), name='request-declined'),
    path('application_list/approved/', AprovedApplicationView.as_view(), name='aproved-applications'),
    path('application_list/denied/', DeniedApplicationView.as_view(), name='aproved-applications'),
    path('application_list/approved/users/', AprovedApplicationView.as_view(), name='aproved-applications'),

    path('application_list/alocate_slot/<int:id>/', AllotedSeat.as_view(), name='seat-allocation'),
    path('application_list/clear_slot/<int:id>/', ClearSeat.as_view(), name='seat-deallocation'),


    path('seat_available/', seat.as_view(), name='seat-display'),



   
    
]