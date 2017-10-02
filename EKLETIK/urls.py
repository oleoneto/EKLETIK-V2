"""

EKLETIK URL Configuration
Written by Leo Neto
Updated on Sept 16, 2017

"""

# Importing Django stuff...
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth.models import User
from django.contrib.auth.views import *
from django.conf import settings
from django.conf.urls.static import static

# Importing application views
from EKSite import mainviews as site
from EKSite import docviews as docs
from EKSite import API as API
from EKSite import searchviews as Search
from EKSite import experimentalProjectViews as ep

# Importing REST API
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    # Admin / Auth / Status Codes Views
    url(r'^401', site.error_401, name='401'),
    url(r'^403', site.error_403, name='403'),
    url(r'^404', site.error_404, name='404'),
    url(r'^405', site.error_405, name='405'),
    url(r'^500', site.error_500, name='500'),
    url(r'^admin.*', site.error_404),
    url(r'^dash.*', site.error_404),
    url(r'^wp.*', site.error_404),
    url(r'^login.*', site.error_404),
    url(r'^i/sys/', admin.site.urls, name='sys'),

    url(r'^i/logout/$', logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^i/login/$', site.userlogin, name='userlogin'),
    url(r'^i/auth/$', site.userauth, name='userauth'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    # MAIN Views
    url(r'^$', site.home, name='home'),
    url(r'^portfolio/(?P<key>\D+)', site.singleProject, name='project'),
    url(r'^portfolio/', site.portfolio, name='portfolio'),
    url(r'^empresa/', site.company, name='company'),
    url(r'^contacto/', site.contact, name='contact'),

    # SEARCH
    url(r'^p/', Search.SearchResults, name='searchResults'),

    #----------

    # DOCS / ARTICLES / BLOG Views
    url(r'^docs/(?P<key>\D+)', docs.singleDoc, name='doc'),
    url(r'^docs/', docs.home, name='docs'),
    url(r'^blog/(?P<key>\D+)', docs.singleDoc, name='post'),
    url(r'^blog/', docs.home, name='posts'),

    #----------

    # API Views
    url(r'^api/docs/(?P<pk>\d+)', API.DocDetailAPIView.as_view()),
    url(r'^api/docs/(?P<slug>[\w-]+)', API.DocDetailAPIViewSlug.as_view()),
    url(r'^api/docs', API.DocListAPIView.as_view()),


    url(r'^api/pessoas/(?P<pk>\d+)', API.PersonDetailAPIView.as_view()),
    url(r'^api/pessoas', API.PersonListAPIView.as_view()),
    url(r'^api/people/(?P<pk>\d+)', API.PersonDetailAPIView.as_view()),
    url(r'^api/people', API.PersonListAPIView.as_view()),

    url(r'^api/portfolio/(?P<pk>\d+)', API.PortfolioProjectDetailAPIView.as_view()),
    url(r'^api/portfolio', API.PortfolioProjectListAPIView.as_view()),

    url(r'^api/cores/', API.ColorListAPIView.as_view()),
    url(r'^api/colors/', API.ColorListAPIView.as_view()),

    #----------


    # PROJECT Views
    url(r'^hora', ep.horas),
    url(r'^horas', ep.horas),
    url(r'^oiseau', ep.horas),
    url(r'^haricot', ep.horas),
    url(r'^morcovi', ep.morcovi),
    url(r'^cartofi', ep.horas),
    url(r'^bot', ep.horas),


    #----------

    # these api endpoints are here for compatibility
    # reasons use main endpoints whenever possible...
    url(r'^api/blog/(?P<pk>\d+)', API.DocDetailAPIView.as_view()),
    url(r'^api/blog', API.DocListAPIView.as_view()),
    url(r'^api/articles/(?P<pk>\d+)', API.DocDetailAPIView.as_view()),
    url(r'^api/articles', API.DocListAPIView.as_view()),
    url(r'^api/projects/(?P<pk>\d+)', API.PortfolioProjectDetailAPIView.as_view()),
    url(r'^api/projects', API.PortfolioProjectListAPIView.as_view()),


    # REDIRECT Views
    url(r'^azinca', site.azinca),
    url(r'^azinka', site.azinca),
    url(r'^m8', site.meight),
    url(r'^mate', site.meight),
    url(r'^meight', site.meight),
    url(r'^django', docs.django),
    url(r'^felipe', site.felipe),
    url(r'^paulo', site.paulo),
    url(r'^leo', site.leo),
    #url(r'^', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# REST API URL Configuration...
urlpatterns = format_suffix_patterns(urlpatterns)