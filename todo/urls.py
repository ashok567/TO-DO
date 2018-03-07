from django.contrib import admin
from django.conf.urls import url
from django.views.generic import RedirectView

from catalog.views import ToDoListView, ToDoDetailView, index


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^api/$', ToDoListView.as_view(), name='apilist'),
    url(r'^api/(?P<pk>\d*)', ToDoDetailView.as_view(), name='apidetail'),
    url(r'', RedirectView.as_view(url='/')),
]
