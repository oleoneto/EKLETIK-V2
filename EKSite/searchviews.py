from ViewsLibraries import *
from .models import *



def SearchProjects(keyword):
    try:
        projects = PortfolioProject.objects.filter(title__icontains=keyword).filter(status='p')
        if not projects:
            projects = PortfolioProject.objects.filter(description__icontains=keyword).filter(status='p')
            if not projects:
                projects = PortfolioProject.objects.filter(author__name__icontains=keyword).filter(status='p')
    except Person.DoesNotExist:
        erro = True
        raise Http404('No project...')
    return projects



def ImprovedDocSearch(keyword):
    try:
        docsbyauthorname = Doc.objects.filter(author__name__icontains=keyword)
        docsbyauthorslug = Doc.objects.filter(author__slug__icontains=keyword)
        docsbyslug   = Doc.objects.filter(slug__icontains=keyword)
        docsbytitle  = Doc.objects.filter(title__icontains=keyword)
        docsbytopic  = Doc.objects.filter(programmingLanguage__icontains=keyword)
        docs = docsbyauthorname + docsbyauthorslug + docsbyslug + docsbytitle + docsbytopic
    except Doc.DoesNotExist:
        raise Http404()
    return docs




# SEARCH in PEOPLE
def SearchPeople(keyword):
    try:
        people = Person.objects.filter(name__icontains=keyword)
        if not people:
            people = Person.objects.filter(name__contains=keyword)
            if not people:
                people = Person.objects.filter(slug__contains=keyword)
                if not people:
                    people = Person.objects.filter(slug__icontains=keyword)
    except Person.DoesNotExist:
        erro = True
        raise Http404('No person...')
    return people



# SEARCH in DOCS
def SearchDocs(keyword, request):
    people = SearchPeople(keyword)
    try:
        docs = Doc.objects.filter(author__name__icontains=keyword).filter(status='p')
        if not docs:
            docs = Doc.objects.filter(author__slug__icontains=keyword).filter(status='p')
        if not docs:
            docs = Doc.objects.filter(title__icontains=keyword).filter(status='p')
            if not docs:
                docs = Doc.objects.filter(slug__icontains=keyword).filter(status='p')
                if not docs:
                    docs = Doc.objects.filter(content__icontains=keyword).filter(status='p')
                    if not docs:
                        docs = Doc.objects.filter(summary__icontains=keyword).filter(status='p')
                        if not docs:
                            docs = Doc.objects.filter(programmingLanguage__icontains=keyword).filter(status='p')
                            if not docs:
                                docs = Doc.objects.filter(author__author_bio__icontains=keyword).filter(status='p')
    except Doc.DoesNotExist:
        erro = True
        raise Http404('Nothing found')
    return docs
















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

    return render(request, '_PT/pesquisa.html', {
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