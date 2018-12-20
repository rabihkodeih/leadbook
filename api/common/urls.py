"""jbe_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.utils.translation import ugettext_lazy as _

from rest_framework.documentation import include_docs_urls

from api import views as api_views


urlpatterns = [
    path(r'admin/', admin.site.urls),
    url(r'', include((api_views.urls, 'api'), namespace='api')),
    url(r'^docs/', include_docs_urls(title='Leadbook API'))
]

# this allows gunicorn (or any external wsgi server) to server static files
urlpatterns += staticfiles_urlpatterns()

# Change admin site title
admin.site.site_header = _('Leadbook API Admin')
admin.site.site_title = _('Leadbook API Admin')


# end of file
