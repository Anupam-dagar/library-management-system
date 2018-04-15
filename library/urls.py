from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^adminpage/$', views.create_user, name='create_user'),
    url(r'^create-student/(?P<username>[\w.@+-]+)/(?P<staff>[\w.@+-]+)$', views.create_student, name='create_student'),
    url(r'^ajax/change_request_issue/$', views.change_request_issue, name='change_request_issue')
]