from ViewsLibraries import *



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

def sonzito(request):
    return render(request, 'Labs/sonzito.html')

def radio(request):
    return render(request, 'Labs/radio.html')

def news(request):
    return render(request, 'Labs/news.html')