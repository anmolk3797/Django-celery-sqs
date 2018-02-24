
from django.conf.urls import url
from django.contrib import admin

from .views import TaskQueuer

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^queue/', TaskQueuer.as_view(), name='task_queuer'),
]
