"""
Written by Leo Neto
Updated on January 4, 2018
http://brython.info/static_doc/en/intro.html?lang=en
http://stephen.band/jparallax/
"""

from LibrariesForViews import *
from EKSite.api_eventbrite import BuildObjects
from EKSite.api_news import NewsObjects
from EKSite.api_spotify import BuildTracks


def ClockViewController(request):
    """
    :param request: HTTP request object
    :return:
    """
    docsArray = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    return render(request, 'labs/hora.html', {
        'docs': docsArray,
    })


def MorcoviiViewController(request):
    """
    :param request: HTTP request object
    :return: specified HTML template
    """
    return render(request, 'labs/morcovi.html')


def LabViewController(request):
    """
    :param request: HTTP request object
    :return: specified HTML template
    """
    return render(request, 'labs/lab.html')


def SpotifyViewController(request):
    """
    :param request: HTTP request object
    :return: an array of audio tracks fetched from Spotify's API
    """
    audios = BuildTracks()
    total = audios.__len__()
    return render(request, 'labs/spotify.html', {
        'page': 'oiseau',
        'audios': audios,
        'total': total,
        'max': 12,
    })


def RadioViewController(request):
    """
    :param request:
    :return: specified HTML template
    """
    return render(request, 'labs/radio.html')


def NewsViewController(request, searchTerm='1'):
    """
    :param request: HTTP request object
    :param searchTerm: a string representing terms to search for in the NewsAPI
    :return: an array of news articles from the NewsAPI
    """
    articlesArray = NewsObjects(searchTerm)

    return render(request, '_PT/news.html', {
        'page': 'NewsViewController',
        'articles': articlesArray,
        'total': len(articlesArray),
    })


def EventsViewController(request, keyword="Indianapolis"):
    """
    :param request:
    :param keyword:
    :return: an array of event objects from the EventBrite API
    """
    objs = BuildObjects(keyword)
    events = objs[0]
    titles = objs[1]
    city = objs[2]

    return render(request, 'labs/eventmate.html', {
        'page': "EventsViewController",
        'events': events,
        'total': len(titles),
        'city': city,
    })


def AjaxViewController(request):
    """
    :param request: HTTP request object
    :return: specified HTML template
    """
    return render(request, 'labs/jax.html', {
        'page': 'AjaxViewController',
    })


def jax_audio(request):
    """
    :param request: HTTP request object
    :return: specified HTML template
    """
    return render(request, 'labs/jax-audio.html', {
        'page': 'AjaxAudioViewController',
    })