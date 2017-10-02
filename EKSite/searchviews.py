from ViewsLibraries import *
from .models import *


















# SEARCH in DOCS
def SearchDocs(title, request):
    try:
        docs = Doc.objects.filter(title__icontains=title).filter(status='p')
        if not docs:
            docs = Doc.objects.filter(slug__icontains=title).filter(status='p')
            if not docs:
                docs = Doc.objects.filter(content__icontains=title).filter(status='p')
                if not docs:
                    docs = Doc.objects.filter(summary__icontains=title).filter(status='p')
                    if not docs:
                        docs = Doc.objects.filter(programmingLanguage__contains=title).filter(status='p')
                        if not docs:
                            docs = Doc.objects.filter(author__name__contains=title).filter(status='p')
                            if not docs:
                                docs = Doc.objects.filter(author__author_bio__icontains=title).filter(status='p')
    except Doc.DoesNotExist:
        erro = True
        raise Http404('Nothing found')
    return docs






# SEARCH in PEOPLE
def SearchPeople(name):
    try:
        people = Person.objects.filter(name__contains=name)
    except Person.DoesNotExist:
        erro = True
        raise Http404('No person...')
    return people


def SearchProjects(title):
    try:
        projects = PortfolioProject.objects.filter(title__icontains=title).filter(status='p')
        if not projects:
            projects = PortfolioProject.objects.filter(description__icontains=title).filter(status='p')
            if not projects:
                projects = PortfolioProject.objects.filter(author__name__icontains=title).filter(status='p')
    except Person.DoesNotExist:
        erro = True
        raise Http404('No project...')
    return projects






##############################################

def SearchResults(request):
    if request.POST:
        requestKeyword = request.POST['keyword']
        docs = SearchDocs(requestKeyword, request)
        people = SearchPeople(requestKeyword)
        projects = SearchProjects(requestKeyword)
        user = 'user'
        erro = False
        totalresults = docs.__len__()+people.__len__()+projects.__len__()
    else:
        return redirect('/')
    if(docs.__len__() == 1):
        if not projects:
            return redirect('/docs/{}'.format(docs[0].slug))
    elif(projects.__len__() == 1):
        if not docs:
            return redirect('/portfolio/{}'.format(projects[0].slug))

    return render(request, 'PT/searchResults.html', {
        'main': 'Pesquisar',
        'pageName': 'Search',
        'r': requestKeyword,
        'erro': erro,
        'search': request.POST['keyword'],
        'docs': docs,
        'people': people,
        'projects': projects,
        'user': user,
        'total': totalresults,
    })

#####################################################