from django.urls import path
from .views import *



urlpatterns = [
    path('signup/', SignUpView, name='signup'),
    path('',LoginView, name='login'),
    path('logout/',LogoutView,name='logout'),
    path('data/', DataView, name='data'),
    path('delete/<int:id>/', DeleteView, name='delete'),
    path('edit/', EditView, name='edit'),
    
]
