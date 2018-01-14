"""

EKLETIK URL Configuration
Written by Leo Neto
Updated on January 4, 2018

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
from EKSite import views_system as system
from EKSite import views_api as API
from EKSite import views_search as search
from EKSite import views_labs as labs
from EKSite import views

# Importing REST API
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # Admin / Auth / Status Codes Views
    url(r'^401', system.error_401, name='401'),
    url(r'^403', system.error_403, name='403'),
    url(r'^404', system.error_404, name='404'),
    url(r'^405', system.error_405, name='405'),
    url(r'^500', system.error_500, name='500'),
    url(r'^admin.*', system.error_404),
    url(r'^dash.*', system.error_404),
    url(r'^wp.*', system.error_404),
    url(r'^login.*', system.error_404),
    url(r'^i/sys/', admin.site.urls, name='sys'),
    url(r'^i/logout/$', logout, {'template_name': 'Masters/logout.html'}, name='logout'),
    url(r'^i/login/$', system.userlogin, name='userlogin'),
    url(r'^i/auth/$', system.userauth, name='userauth'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^register/$', system.register, name='register'),


    # MAIN Views
    url(r'^$', views.IndexViewController, name='home'),
    url(r'^portfolio/(?P<slug>\D+)', views.PortfolioSingleViewController, name='project'),
    url(r'^portfolio/', views.PortfolioViewController, name='portfolio'),
    url(r'^empresa/', views.CompanyViewController, name='company'),

    url(r'^events/(?P<keyword>\D+)', labs.EventsViewController, name='events'),
    url(r'^events/(?P<keyword>\d+)', labs.EventsViewController, name='events'),
    url(r'^events/', labs.EventsViewController, name='events'),
    url(r'^spotify/', labs.SpotifyViewController),

    url(r'^news/(?P<keyword>\D+)', labs.NewsViewController, name='news'),
    url(r'^news/', labs.NewsViewController, name='news'),

    # SEARCH Views
    url(r'^p/', search.SearchViewController, name='searchResults'),
    url(r'^pesquisar|search', search.SearchViewController, name='search'),

    #----------

    # DOCUMENTATION Views
    url(r'^docs/autor/(?P<key>\D+)', views.DocAuthorViewController, name='docAuthor'),
    url(r'^docs/(?P<slug>\D+)/edit', views.DocEditViewController, name="doc-edit"),
    url(r'^docs/(?P<slug>\D+)', views.DocSingleViewController, name='doc'),
    url(r'^docs/', views.DocGeneralViewController, name='docs'),

    url(r'^post/create', views.DocCreateViewController, name='doc-create'),


    url(r'^blog/author/(?P<key>\D+)', views.DocAuthorViewController, name='postAuthor'),
    url(r'^blog/(?P<slug>\D+)', views.DocSingleViewController, name='post'),
    url(r'^blog/', views.DocGeneralViewController, name='posts'),

    #----------

    # API Views
    url(r'^api/docs/(?P<pk>\d+)', API.DocDetailAPIView.as_view()),
    url(r'^api/docs/(?P<slug>[\w-]+)', API.DocDetailAPIViewSlug.as_view()),
    url(r'^api/docs', API.DocListAPIView.as_view()),

    url(r'^api/pessoas/(?P<pk>\d+)', API.PersonDetailAPIView.as_view()),
    url(r'^api/pessoas/(?P<slug>\D+)', API.PersonDetailAPIViewSlug.as_view()),
    url(r'^api/pessoas', API.PersonListAPIView.as_view()),
    url(r'^api/people/(?P<pk>\d+)', API.PersonDetailAPIView.as_view()),
    url(r'^api/people/(?P<slug>\D+)', API.PersonDetailAPIViewSlug.as_view()),
    url(r'^api/people', API.PersonListAPIView.as_view()),

    url(r'^api/portfolio/(?P<pk>\d+)', API.PortfolioProjectDetailAPIView.as_view()),
    url(r'^api/portfolio/(?P<slug>\D+)', API.PortfolioProjectDetailAPIViewSlug.as_view()),
    url(r'^api/portfolio', API.PortfolioProjectListAPIView.as_view()),

    url(r'^api/cores/', API.ColorListAPIView.as_view()),
    url(r'^api/colors/', API.ColorListAPIView.as_view()),

    url(r'^api/audios/(?P<slug>\D+)', API.AudioDetailAPIViewSlug.as_view()),
    url(r'^api/audios/(?P<pk>\d+)', API.AudioDetailAPIView.as_view()),
    url(r'^api/audios/', API.AudioListAPIView.as_view()),


    #-----------------------------
    # These api endpoints are here for compatibility reasons.
    # Use main endpoints whenever possible...
    url(r'^api/blog/(?P<pk>\d+)', API.DocDetailAPIView.as_view()),
    url(r'^api/blog', API.DocListAPIView.as_view()),
    url(r'^api/articles/(?P<pk>\d+)', API.DocDetailAPIView.as_view()),
    url(r'^api/articles', API.DocListAPIView.as_view()),
    url(r'^api/projects/(?P<pk>\d+)', API.PortfolioProjectDetailAPIView.as_view()),
    url(r'^api/projects', API.PortfolioProjectListAPIView.as_view()),


    #-----------------------------
    # LAB Views
    url(r'^labs/relogio/', labs.ClockViewController, name="relogio"),
    url(r'^labs/oiseau/', labs.SpotifyViewController, name="spotify"),
    url(r'^labs/RadioViewController/', labs.RadioViewController, name="radio"),
    url(r'^labs/haricots/', labs.ClockViewController, name="haricots"),
    url(r'^labs/morcovi/', labs.MorcoviiViewController, name="morcovi"),
    url(r'^labs/cartofi/', labs.ClockViewController, name="cartofi"),
    url(r'^labs/bot/', labs.ClockViewController, name="bot"),
    url(r'^labs/news/', labs.NewsViewController, name='newslab'),
    url(r'^labs/audio/', labs.jax_audio, name='audio'),
    url(r'^labs/jax/', labs.AjaxViewController, name='jax'),
    url(r'^labs/', labs.LabViewController, name="labs"),


    # REDIRECT Views
    url(r'^azinca|azinka|azinco|azinc|azink', system.azinca),
    url(r'^mate|m8|meight', system.meight),
    url(r'^django', views.DocViewControllerForDjangoTutorial),
    url(r'^felipe', system.felipe),
    url(r'^paulo', system.paulo),
    url(r'^leo', system.leo),
    url(r'^git|github|bitbucket|source', system.source_control),
    #url(r'^', include(router.urls)),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# REST API URL Configuration...
urlpatterns = format_suffix_patterns(urlpatterns)