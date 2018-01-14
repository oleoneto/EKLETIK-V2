"""
Written by Leo Neto
Updated on January 4, 2018
"""

from LibrariesForViews import *
from .models import *


def SearchInDocs(keyword):
    tempArray = []
    docsArray = []

    try:
        docsbyauthorname = Doc.objects.filter(author__name__icontains=keyword)
        if docsbyauthorname:
            tempArray.append(docsbyauthorname)

        docsbyauthorslug = Doc.objects.filter(author__slug__icontains=keyword)
        if docsbyauthorslug:
            tempArray.append(docsbyauthorslug)

        docsbyslug   = Doc.objects.filter(slug__icontains=keyword)
        if docsbyslug:
            tempArray.append(docsbyslug)

        docsbytitle  = Doc.objects.filter(title__icontains=keyword)
        if docsbytitle:
            tempArray.append(docsbytitle)

        docsbytopic  = Doc.objects.filter(programmingLanguage__icontains=keyword)
        if docsbytopic:
            tempArray.append(docsbytopic)

        docsbycontent = Doc.objects.filter(content__icontains=keyword)
        if docsbycontent:
            tempArray.append(docsbycontent)

        for set in tempArray:
            for obj in set:
                if obj not in docsArray:
                    docsArray.append(obj)

        # for set in docsArray:
        #     for obj in set:
        #         if obj.title > obj

    except Doc.DoesNotExist:
        raise Http404()
    return docsArray


def SearchInProjects(keyword):
    tempArray = []
    projectsArray = []

    try:
        projectsbyauthorname = PortfolioProject.objects.filter(author__name__icontains=keyword)
        if projectsbyauthorname:
            tempArray.append(projectsbyauthorname)

        projectsbyauthorslug = PortfolioProject.objects.filter(author__slug__icontains=keyword)
        if projectsbyauthorslug:
            tempArray.append(projectsbyauthorslug)

        projectsbyslug = PortfolioProject.objects.filter(slug__icontains=keyword)
        if projectsbyslug:
            tempArray.append(projectsbyslug)

        projectsbytitle = PortfolioProject.objects.filter(title__icontains=keyword)
        if projectsbytitle:
            tempArray.append(projectsbytitle)

        projectsbytype = PortfolioProject.objects.filter(type__icontains=keyword)
        if projectsbytype:
            tempArray.append(projectsbytype)

        projectsbycontent = PortfolioProject.objects.filter(description__icontains=keyword)
        if projectsbycontent:
            tempArray.append(projectsbycontent)

        for set in tempArray:
            for obj in set:
                if obj not in projectsArray:
                    projectsArray.append(obj)


    except PortfolioProject.DoesNotExist:
        raise Http404()
    return projectsArray


def SearchInPeople(keyword):
    tempArray = []
    peopleArray = []

    try:
        peoplebyname = Person.objects.filter(name__icontains=keyword)
        if peoplebyname:
            tempArray.append(peoplebyname)

        peoplebyslug = Person.objects.filter(slug__icontains=keyword)
        if peoplebyslug:
            tempArray.append(peoplebyslug)

        peoplebyposition = Person.objects.filter(position__icontains=keyword)
        if peoplebyposition:
            tempArray.append(peoplebyposition)

        peoplebybio = Person.objects.filter(bio__icontains=keyword)
        if peoplebybio:
            tempArray.append(peoplebybio)

        peoplebyauthorbio = Person.objects.filter(author_bio__icontains=keyword)
        if peoplebyauthorbio:
            tempArray.append(peoplebyauthorbio)

        for set in tempArray:
            for obj in set:
                if obj not in peopleArray:
                    peopleArray.append(obj)


    except PortfolioProject.DoesNotExist:
        raise Http404()
    return peopleArray


def SearchViewController(request):

    """
    :param request: HTTP Request
    :return: multiple arrays with all available model objects [note: return types are not QuerySets]
    """

    """
    Restricted access to the search results page for only when the HTTP Request is through a POST.
    If not the case, the browser should return the same template with variables set to default values.
    """
    if request.POST:

        searchTerm = request.POST['keyword']

        docs     = SearchInDocs(searchTerm)
        docsTotal = docs.__len__()

        projects = SearchInProjects(searchTerm)
        projectsTotal = projects.__len__()

        people   = SearchInPeople(searchTerm)
        peopleTotal = people.__len__()

        totalResults = docsTotal + projectsTotal + peopleTotal

        # if total > 1:
        message = 'A pesquisa por <code class="text-bold">{}</code> retornou {} resultados'.format(searchTerm, totalResults)

    else:
       return render(request, '_PT/search.html', {
           'main': 'Pesquisar',
           'page': 'Search',
           'search': None,
           'total': None,
       })

    if(docsTotal == 1):
        if not projects:
            return redirect('/docs/{}'.format(docs[0].slug))
    elif(projectsTotal == 1):
        if not docs:
            return redirect('/portfolio/{}'.format(projects[0].slug))
    elif(peopleTotal == 1):
        if Doc.objects.filter(author_id=people[0].id):
            return redirect('/docs/autor/{}'.format(people[0].slug))


    return render(request, '_PT/search.html', {
        'main': 'Pesquisar',
        'page': 'Search',
        'search': searchTerm,
        'docs': docs,
        'people': people,
        'projects': projects,
        'total': totalResults,
        'message': message,
    })