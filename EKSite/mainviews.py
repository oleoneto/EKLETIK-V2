from ViewsLibraries import *
from .models import *
from .forms import *

"""

Written by Leo Neto
Updated on Sept 16, 2017

"""




################ ERRORS #####################


def error_report(errorMessage):
    pass

def error_401(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, 'Masters/401.html', {
        'origin': requestOrigin,
        'pageName': '401',
        'docs': docs,
    })

def error_403(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, 'Masters/403.html', {
        'origin': requestOrigin,
        'pageName': '403',
        'docs': docs,
    })

def error_404(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, 'Masters/404.html', {
        'origin': requestOrigin,
        'pageName': '404',
        'docs': docs,
    })

def error_405(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, 'Masters/405.html', {
        'origin': requestOrigin,
        'pageName': '405',
        'docs': docs,
    })

def error_500(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, 'Masters/500.html', {
        'origin': requestOrigin,
        'pageName': '500',
        'docs': docs,
    })


#_______________ LOGIN ___________________
def userlogin(request):
    return render(request, 'Masters/loginPT.html')

def userauth(request):
    session_username = request.POST['username']
    session_password = request.POST['password']
    user = authenticate(request, username=session_username, password=session_password)
    if user is not None:
        login(request, user)
        # print(reverse('admin:EKSite'))
        return redirect('/i/sys/')
    else:
        return render(request, 'Masters/500.html')









#______________ MAIN SITE ________________

def home(request):
    # if request.LANGUAGE_CODE !=
    persons = Person.objects.filter(status='p').order_by('name')
    projects = PortfolioProject.objects.filter(status='p').filter(featured=True)
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    total = projects.count()
    grid = 'col-lg-4 col-md-4 col-sm-12'

    return render(request, 'PT/index.html', {
        'pageName': 'home',
        'persons': persons,
        'projects': projects,
        'docs': docs,
        'project_max': 3,
        'doc_max': 4,
        'grid': grid,
    })

def company(request):
    people = Person.objects.filter(board_member=True).order_by('name')
    total = people.count()

    if total%3 == 0:
        grid = 'col-lg-4 col-md-4 col-sm-12'
    elif total%2 == 0:
        grid = 'col-lg-3 col-md-3 col-sm-12'
    else:
        grid = 'col-lg-4 col-md-4 col-sm-12'

    return render(request, 'PT/empresa.html', {
        'pageName': 'empresa',
        'people': people,
        'totalPeople': total,
        'grid': grid,
    })

def portfolio(request):
    projects = PortfolioProject.objects.filter(status='p').order_by('-publishedDate')
    featured = PortfolioProject.objects.filter(status='p').filter(featured=True)
    total = projects.count()
    grid = 'col-lg-4 col-md-4 col-sm-12'

    # This condition is not relevant yet
    # will check for something else later
    if total%3 == 0:
        grid = 'col-lg-4 col-md-4 col-sm-12'

    return render(request, 'PT/portfolio.html', {
        'page': 'portfolio-home',
        'projects': projects,
        'featured': featured,
        'featuredTotal': featured.count(),
        'project_max': 1000,
        'featured_max': 3,
        'grid': grid,
    })

def singleProject(request, key):
    try:
        project = PortfolioProject.objects.get(slug=key)
    except PortfolioProject.DoesNotExist:
        raise Http404('No Project')

    try:
        colors = Color.objects.filter(projectName=project.id).order_by('hexColor')
    except Color.DoesNotExist:
        raise Http404('No Colors')
    try:
        photos = Photo.objects.filter(projectName=project.id)
    except Photo.DoesNotExist:
        raise Http404('No Photos')
    try:
        audios = Audio.objects.filter(project=project.id).order_by('number')
    except Audio.DoesNotExist:
        raise Http404('No Audio')

    return render(request, 'PT/portfolio.html', {
        'page': 'portfolio-single',
        'project': project,
        'client': project.client,
        'title': project.title,
        'type': project.type,
        'artwork': project.artwork.url,
        'description': project.description,
        'colors': colors,
        'photos': photos,
        'audios': audios,
    })

def contact(request):
    formClass = ContactForm
    return render(request, 'PT/contacto.html', {
        'pageName': 'contacto',
        'form': formClass,
        'choices': SOLICIT_CHOICES,
    })

def message(request):
    formClass = MessageForm
    return render(request, 'PT/mensagem.html', {
        'pageName': 'mensagem',
        'form': formClass,
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

def leo(request):
    return redirect('https://github.com/oleoneto')

def paulo(request):
    return redirect('https://github.com/pjaime88')

def felipe(request):
    return redirect('https://github.com/fsilva24')



#------ Other Projects -------
# Check experimentalProjectViews.py


