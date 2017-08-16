from django.conf.urls import url

from .views import index, tasks_list


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^tasks-list/$', tasks_list, name='tasks_list'),
]
