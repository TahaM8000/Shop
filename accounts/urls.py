from django.urls import path, include
from .api_views import *


urlpatterns = [
    path('user/create/', user_create, name='user_create'),
    path('user/update/<slug:phoneNumber>/', user_update, name='user_update'),
    # path('login/', login_view, name="api-auth-login"),
    # path('user/code/again/<slug:phoneNumber>/', code_get, name='code_get'),
    # path('user/change/password/<slug:phoneNumber>/',
    #      change_password, name='change_password'),
    # path('user/change/password2/<slug:phoneNumber>/',
    #      change_password_without_old, name='change_password_without_old'),
    # path('', include('rest_framework.urls')),
    # path('user/info/<slug:phoneNumber>/', user_get, name='user_get'),
    # path('csrf/', get_csrf_token.as_view(), name='csrf'),
]
