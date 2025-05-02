
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import logout_view


urlpatterns = [
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', logout_view, name='api_logout'),
]
