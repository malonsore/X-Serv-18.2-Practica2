from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Practica2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^(.*)$', 'Practica2app.views.Practica2'),
 	url(r'^admin/', include(admin.site.urls)),
)
