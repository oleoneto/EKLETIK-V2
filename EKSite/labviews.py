from ViewsLibraries import *
from EKSite.ExternalAPIs import *

"""

Written by Leo Neto
Updated on Sept 16, 2017

"""





def horas(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    return render(request, 'Labs/hora.html', {
        'docs': docs,
    })

def morcovii(request):
    return render(request, 'Labs/morcovi.html')

def experimentos(request):
    return render(request, 'Labs/labs.html')

def musicplayer(request):
    return render(request, 'Labs/oiseau.html')

def radio(request):
    return render(request, 'Labs/radio.html')

def news(request):
    articles = NewsObjects()
    return render(request, 'Labs/news.html', {
        'page': 'news',
        'articles': articles,
        'total': len(articles),
    })

def eventmate(request):
    objs = BuildObjects()
    events = objs[0]
    titles = objs[1]
    city = objs[2]

    return render(request, 'Labs/eventmate.html', {
        'page': "eventmate",
        'events': events,
        'total': len(titles),
        'city': city,
    })


def jax(request):
    return render(request, 'Labs/jax.html')

def jax_audio(request):
    return render(request, 'Labs/jax-audio.html')