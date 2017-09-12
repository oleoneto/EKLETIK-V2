from ViewsLibraries import *
from .models import *




################ ERRORS #####################


def error_report(errorMessage):
    pass

def error_401(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, '401.html', {
        'origin': requestOrigin,
        'pageName': '401',
        'docs': docs,
    })

def error_403(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, '403.html', {
        'origin': requestOrigin,
        'pageName': '403',
        'docs': docs,
    })


def error_404(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, '404.html', {
        'origin': requestOrigin,
        'pageName': '404',
        'docs': docs,
    })

def error_405(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, '405.html', {
        'origin': requestOrigin,
        'pageName': '405',
        'docs': docs,
    })

def error_500(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, '500.html', {
        'origin': requestOrigin,
        'pageName': '500',
        'docs': docs,
    })

# if session is secure, try logging in the user
# if the session is not secure, raise a 401
def login_authentication(request):
    requestOrigin = request.get_full_path()
    if request.is_secure():
        if request.user.is_authenticated:
            return redirect('/')
    else:
        error_401(request)

def login(request):
    requestOrigin = request.get_full_path()
    return render(request, 'loginPT.html')



















#______________ MAIN SITE ________________

def home(request):
    persons = Person.objects.filter(status='p').order_by('name')
    projects = PortfolioProject.objects.filter(status='p').order_by('-publishedDate').filter(featured=True)
    featured = FeaturedHeader.objects.order_by('id')
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    return render(request, 'PT/index.html', {
        'pageName': 'home',
        'persons': persons,
        'projects': projects,
        'featured': featured,
        'featuredTotal': featured.__sizeof__(),
        'docs': docs,
    })

def company(request):
    people = Person.objects.filter(board_member=True).order_by('name')
    return render(request, 'PT/empresa.html', {
        'pageName': 'empresa',
        'people': people,
    })

def portfolio(request):
    projects = PortfolioProject.objects.filter(status='p').order_by('-publishedDate')
    return render(request, 'PT/portfolio.html', {
        'pageName': 'portfolio',
        'projects': projects,
    })

def singleProject(request, key):
    try:
        project = PortfolioProject.objects.get(slug=key)
    except PortfolioProject.DoesNotExist:
        raise Http404('No Project')

    try:
        colors = Color.objects.filter(projectName=project.id)
    except Color.DoesNotExist:
        raise Http404('No Colors')
    try:
        photos = Photo.objects.filter(projectName=project.id)
    except Photo.DoesNotExist:
        raise Http404('No Photos')

    return render(request, 'PT/portfolio-single.html', {
        'pageName': 'portfolio',
        'project': project,
        'client': project.client,
        'title': project.title,
        'type': project.type,
        'artwork': project.artwork.url,
        'description': project.description,
        'colors': colors,
        'photos': photos,
    })


def contact(request):
    return render(request, 'PT/contacto.html', {
        'pageName': 'contacto',
        'choices': SOLICIT_CHOICES,
    })




#----------- SEARCH ----------------

def searchResults(request):
    return render(request, 'PT/searchResults.html', {
        'pageName': 'results',
    })









#--------- REDIRECTS --------------
def azinca(request):
    return redirect('https://www.youtube.com/channel/UCxAIq85nPCo1whr8KYwVJkA')
def meight(request):
    return redirect('https://github.com/Ngola')




#------ Outros Projectos -------
def horas(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    return render(request, 'PT/hora.html',{
        'docs': docs,
    })