from ViewsLibraries import *
from .models import *

















def SearchUsers(name):
    return "User...."


def SearchDocs(title):
    try:
        docs = Doc.objects.filter(title__icontains=title)
        if not docs:
            docs = Doc.objects.filter(content__icontains=title)
            if not docs:
                docs = Doc.objects.filter(summary__icontains=title)
                if not docs:
                    docs = Doc.objects.filter(programmingLanguage__contains=title)
                    if not docs:
                        docs = Doc.objects.filter(author__name__contains=title)
                        if not docs:
                            docs = Doc.objects.filter(author__author_bio__icontains=title)
    except Doc.DoesNotExist:
        erro = True
        raise Http404('Nothing found')
    return docs


def SearchPeople(name):
    try:
        people = Person.objects.filter(name__contains=name)
    except Person.DoesNotExist:
        erro = True
        raise Http404('No person...')
    return people

def SearchProjects(title):
    try:
        projects = PortfolioProject.objects.filter(title__icontains=title)
        if not projects:
            projects = PortfolioProject.objects.filter(description__icontains=title)
            if not projects:
                projects = PortfolioProject.objects.filter(author__name__icontains=title)
    except Person.DoesNotExist:
        erro = True
        raise Http404('No project...')
    return projects

################# Search Views....


def SearchResults(request):
    if request.POST:
        r = request.POST['keyword']
        erro = False
        docs = SearchDocs(r)
        people = SearchPeople(r)
        projects = SearchProjects(r)
        user = 'user'
    else:
        r = 'POST não recebido'
        erro = True
        user = 'None'
    if(docs.__len__() == 1):
        if not projects:
            return redirect('/docs/{}'.format(docs[0].slug))
    elif(projects.__len__() == 1):
        if not docs:
            return redirect('/portfolio/{}'.format(projects[0].slug))


    return render(request, 'PT/searchResults.html', {
        'main': 'Pesquisar',
        'pageName': 'Search',
        'r': r,
        'erro': erro,
        'search': request.POST['keyword'],
        'docs': docs,
        'people': people,
        'projects': projects,
        'user': user,
    })


#####################################################