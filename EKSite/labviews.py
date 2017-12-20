from ViewsLibraries import *
from EKSite.api_eventbrite import BuildObjects
from EKSite.api_news import NewsObjects
from EKSite.api_spotify import BuildTracks



"""

Written by Leo Neto
Updated on Dec 3, 2017
http://brython.info/static_doc/en/intro.html?lang=en
http://stephen.band/jparallax/

"""





def horas(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    return render(request, 'labs/hora.html', {
        'docs': docs,
    })

def morcovii(request):
    return render(request, 'labs/morcovi.html')

def experimentos(request):
    return render(request, 'labs/labs.html')

def musicplayer(request):
    audios = BuildTracks()
    total = 10
    return render(request, 'labs/spotify.html', {
        'page': 'oiseau',
        'audios': audios.__reversed__(),
        'total': total,
        'max': 12,
    })

def radio(request):
    return render(request, 'labs/radio.html')

def news(request, keyword="1"):
    articles = NewsObjects(keyword)

    return render(request, 'labs/news.html', {
        'page': 'news',
        'articles': articles,
        'total': len(articles),
    })

def eventmate(request, keyword="Indianapolis"):
    objs = BuildObjects(keyword)
    events = objs[0]
    titles = objs[1]
    city = objs[2]

    return render(request, 'labs/eventmate.html', {
        'page': "eventmate",
        'events': events,
        'total': len(titles),
        'city': city,
    })

def jax(request):
    return render(request, 'labs/jax.html')

def jax_audio(request):
    return render(request, 'labs/jax-audio.html')