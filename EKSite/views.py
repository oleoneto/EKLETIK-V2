"""

Written by Leo Neto
Updated on January 4, 2018

"""

from LibrariesForViews import *
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404


def Doc_detail(request, slug):
    doc = get_object_or_404(Doc, slug=slug)
    context = {
        'pageName': 'DocSingleViewController',
        'doc': doc,
        'title': doc.title,
        'content': doc.content,
        'author': doc.get_author(),
        'authorSlug': doc.author.get_slug(),
        'authorID': doc.author_id,
        'authorPhoto': doc.author.photo.url,
        'authorGithub': doc.author.github_username,
        'authorBio': doc.author.author_bio,
        # 'authorTotal': authorTotal,
        'language': doc.get_programmingLanguage_display(),
        'date': doc.publishedDate,
        'id': doc.id,
        # 'relateddocs': relateddocs,
    }
    return render(request, "_PT/docs.html", context)


def IndexViewController(request):
    """
    :param request: HTTP Request
    :return: three QuerySets with Person, Docs, and PortfolioProject objects.
    """

    teamMembers = Person.objects.filter(status='p').order_by('name')
    projects = PortfolioProject.objects.filter(status='p').filter(featured=True).order_by('-publishedDate')
    docsInPortuguese = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')

    projectsTotal = projects.count()
    projectsCSSGrid = 'col-lg-4 col-md-4 col-sm-12'
    docsCSSGrid = 'col-md-3 border-none'

    return render(request, '_PT/index.html', {
        'pageName': 'IndexViewController',
        'teamMembers': teamMembers,
        'projects': projects,
        'projectMax': 3,
        'projectsTotal': projectsTotal,
        'docsInPortuguese': docsInPortuguese,
        'docMax': 4,
        'projectsCSSGrid': projectsCSSGrid,
        'docsCSS': docsCSSGrid,
    })


def CompanyViewController(request):
    """
    :param request: HTTP Request
    :return: single QuerySet of Person objects
    """

    teamMembers = Person.objects.filter(board_member=True).order_by('name')
    teamMembersTotal = teamMembers.count()

    if teamMembersTotal%5 == 0:
        teamMembersCSSGrid = 'col-md-2 mr-auto'
    else:
        teamMembersCSSGrid = 'col-md-3 mr-auto'

    return render(request, '_PT/company.html', {
        'pageName': 'CompanyViewController',
        'teamMembers': teamMembers,
        'teamMembersTotal': teamMembers.count(),
        'teamMembersCSSGrid': teamMembersCSSGrid,
    })


def PortfolioViewController(request):
    """
    :param request: HTTP Request
    :return: single QuerySet of PortfolioProject objects
    """

    projects = PortfolioProject.objects.filter(status='p').order_by('-publishedDate')

    return render(request, '_PT/portfolio.html', {
        'page': 'PortfolioViewController',
        'projects': projects,
        'projectsTotal': projects.count(),
        'projectMax': 50,
        'featured': projects.filter(featured=True),
        'featuredTotal': projects.filter(featured=True).count(),
        'featuredMax': 3,
        'projectsCSSGrid': 'col-lg-4 col-md-4 col-sm-12',
    })


def PortfolioSingleViewController(request, slug):
    """
    :param request: HTTP Request
    :param slug: a string that matches a URL-friendly version of the project's title. Ex.: french-skills-app.
    :return: returns a single PortfolioProject object based on the requested slug parameter.
    If the project contains db foreign keys for Color, Photo, and/or Audio objects, those matches are also returned.
    """

    try:
        project = PortfolioProject.objects.get(slug=slug)
    except PortfolioProject.DoesNotExist:
        raise Http404('No Project')

    try:
        projectColors = Color.objects.filter(related_project=project.id).order_by('hexColor')
    except Color.DoesNotExist:
        raise Http404('No Colors')

    try:
        projectPhotos = Photo.objects.filter(related_project=project.id)
    except Photo.DoesNotExist:
        raise Http404('No Photos')

    try:
        projectAudios = Audio.objects.filter(related_project=project.id).order_by('number')
    except Audio.DoesNotExist:
        raise Http404('No Audio')

    return render(request, '_PT/portfolio.html', {
        'page': 'PortfolioSingleViewController',
        'project': project,
        'client': project.client,
        'title': project.title,
        'type': project.type,
        'artwork': project.artwork.url,
        'description': project.description,
        'colors': projectColors,
        'photos': projectPhotos,
        'audios': projectAudios,
    })


def DocGeneralViewController(request):
    """
    Fetches all instances of Doc object-types from the database;
    :param request: HTTP Request Object
    :return: mainly two QuerySets based on the language attribute. One in PT and the other in EN.
    """
    docsInPortuguese = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    docsInEnglish = Doc.objects.filter(status='p').filter(language='en').order_by('-publishedDate')

    docsCSS = 'col-md-4 border-bottom-only'

    return render(request, '_PT/docs.html', {
        'page': 'DocGeneralViewController',
        'docMax': 100,
        'docsInPortuguese': docsInPortuguese,
        'docsInEnglish': docsInEnglish,
        'docsCSS': docsCSS,
    })


def DocSingleViewController(request, slug):
    """
    :param request:
    :param slug:
    :return:
    """

    if 'gs' in slug:
        relateddocs = Doc.objects.filter(status='p').order_by('-publishedDate')
    else:
        relateddocs = Doc.objects.filter(status='p').order_by('-publishedDate').filter(language='pt')

    try:
        doc = Doc.objects.get(slug=slug)
        authorID = doc.author_id
        authorTotal = Doc.objects.filter(author=authorID).filter(status='p').count()
    except Doc.DoesNotExist:
        raise Http404('404 - Doc not found', {'pageName': '404'})

    return render(request, '_PT/docs.html', {
        'pageName': 'DocSingleViewController',
        'doc': doc,
        'author': doc.author,
        'totalByAuthor': authorTotal,
        'relateddocs': relateddocs,
    })


def DocCreateViewController(request):
    """
    :param request:
    :param slug:
    :return:
    """

    context = {
        'pageName': 'DocCreateViewController',
        'form': DocForm(),
    }

    return render(request, '_PT/docs.html', context)


def DocEditViewController(request, slug):
    """
    :param request:
    :param slug:
    :return:
    """
    if request.user.is_authenticated:
        doc = get_object_or_404(Doc, slug=slug)
    else:
        return redirect("/")

    context = {
        'pageName': 'DocEditViewController',
        'form': DocForm(instance=doc),
        'doc': doc,
    }

    return render(request, '_PT/docs.html', context)



def DocAuthorViewController(request, key):
    """
    :param request:
    :param key:
    :return:
    """
    try:
        author = Person.objects.get(slug=key)
        docs = Doc.objects.filter(author__slug=key).order_by('-publishedDate').filter(status='p')
    except Doc.DoesNotExist:
        raise Http404('Author has no DocGeneralViewController')

    return render(request, '_PT/docs.html', {
        'pageName': 'DocAuthorViewController',
        'docs': docs,
        'author': author,
        'authorPhoto': author.photo.url,
        'authorBio': author.author_bio,
        'authorGithub': author.github_username,
    })


def DocViewControllerForDjangoTutorial(request):
    """
    :param request:
    :return:
    """

    key = "gswd"
    authordocs = Doc.objects.filter(author__name=key).filter(status='p')
    relateddocs = Doc.objects.filter(status='p').order_by('-publishedDate')
    try:
        doc = Doc.objects.get(slug=key)
    except Doc.DoesNotExist:
        raise Http404('Doc 404')
    return render(request, '_PT/docs.html', {
        'pageName': 'DocSingleViewController',
        'doc': doc,
        'title': doc.title,
        'content': doc.content,
        'author': doc.get_author(),
        'authorID': doc.author_id,
        'authorPhoto': doc.author.photo.url,
        'authorGithub': doc.author.github_username,
        'authorBio': doc.author.author_bio,
        'language': doc.get_programmingLanguage_display(),
        'date': doc.publishedDate,
        'id': doc.id,
        'authordocs': authordocs,
        'relateddocs': relateddocs,
    })