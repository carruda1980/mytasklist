from django.conf.urls import url
from tasklists.views import CreateTask, Dashboard, DeleteTask, EditTask, GetEditTask,Login, Logout
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create/$', CreateTask.as_view(), name='create'),
    url(r'^dashboard/$', Dashboard.as_view(), name='dashboard'),
    url(r'^delete/$', DeleteTask.as_view(), name='delete'),
    url(r'^edit/$', EditTask.as_view(), name='edit'),
    url(r'^getedit/$', GetEditTask.as_view(), name='getedit'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
]
