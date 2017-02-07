from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^(?P<id>\d+)/$',views.detail,name="detail"),
    url(r'^create/$',views.post_create,name="create"),
    url(r'^(?P<id>\d+)/update/$',views.post_update,name="update"),
    url(r'^(?P<id>\d+)/delete/$',views.post_delete,name="delete"),
]

