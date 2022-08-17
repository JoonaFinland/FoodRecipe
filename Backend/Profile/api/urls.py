from django.conf.urls import url
from .views import *

app_name = 'api-profile'

urlpatterns = [
    url(r'^(?P<id>\d+)/$', ProfileRudView.as_view(), name='rud'),
    url(r'^$', MyProfileView.as_view(({'get': 'list'})), name='my'),
    url(r'^signup/$', new_sign_up_view, name='signup'),
    url(r'^patch/$', patch_meeting, name='patch-p'),
    url(r'^reset-password/$', reset_password, name='reset-p'),
    url(r'^ex/(?P<backend>[^/]+)/$', exchange_token, name='exchange_token'),
    url(r'^zoom-auth/$', zoom_auth, name='zoom_auth'),
    url(r'^zoom-active/$', zoom_active, name='zoom_active'),
]
