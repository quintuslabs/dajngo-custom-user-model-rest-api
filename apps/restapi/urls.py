from django.conf.urls import url

from apps.restapi.views.users import UserCreateAPIView, UserLoginAPIView

urlpatterns = [
    url(r'^users/register/$', UserCreateAPIView.as_view(), name='user-register'),
    url(r'^users/login/$', UserLoginAPIView.as_view(), name="user-login"),
]
