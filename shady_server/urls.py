from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import shady_site.views

# Examples:
# url(r'^$', 'shady_server.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', shady_site.views.index, name='index'),
    path('admin/', admin.site.urls),
]
