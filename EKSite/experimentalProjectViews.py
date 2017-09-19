from ViewsLibraries import *



"""

Written by Leo Neto
Updated on Sept 16, 2017

"""





def horas(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    return render(request, 'PT/hora.html',{
        'docs': docs,
    })

def morcovi(request):
    return render(request, 'PT/morcovi.html')