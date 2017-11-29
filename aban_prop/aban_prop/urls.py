from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

from properties import views as core_views


from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'propertieslist', core_views.PropertiesViewSet)


urlpatterns = [
	url(r'^$', core_views.properties, name='properties'),
	url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^aboutus/$', core_views.aboutus, name='aboutus'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^approveproperties/$', core_views.approveproperties, name='approveproperties'),
    url(r'^properties/details/(?P<id>\w{0,50})/$', core_views.propdetails, name='propdetails'),
    url(r'^propertiessubmit/details/(?P<id>\w{0,50})/$', core_views.propsubdetails, name='propsubdetails'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^settings/password/$', core_views.password, name='password'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
   

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
