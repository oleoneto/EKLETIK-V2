from ViewsLibraries import *
from .models import *
from .forms import *
from .api_news import NewsObjects
# from .api_eventbrite import BuildObjects

"""

Written by Leo Neto
Updated on December 3, 2017

"""




################ ERRORS #####################


def error_report(errorMessage):
    pass

def error_401(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, '401.html', {
        'origin': requestOrigin.replace("/", ""),
        'pageName': '401',
        'docs': docs,
    })

def error_403(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, '403.html', {
        'origin': requestOrigin.replace("/", ""),
        'pageName': '403',
        'docs': docs,
    })

def error_404(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, '404.html', {
        'origin': requestOrigin.replace("/", ""),
        'pageName': '404',
        'docs': docs,
    })

def error_405(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, '405.html', {
        'origin': requestOrigin.replace("/", ""),
        'pageName': '405',
        'docs': docs,
    })

def error_500(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, '500.html', {
        'origin': requestOrigin.replace("/", ""),
        'pageName': '500',
        'docs': docs,
    })






#_______________ LOGIN ___________________
def userlogin(request):
    return render(request, 'masters/loginPT.html')

def userauth(request):
    session_username = request.POST['username']
    session_password = request.POST['password']
    user = authenticate(request, username=session_username, password=session_password)
    if user is not None:
        login(request, user)
        # print(reverse('admin:EKSite'))
        return redirect('/i/sys/')
    else:
        return render(request, '500.html')




#_______________REGISTER___________________

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:home'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, '_PT/registro.html', args)





#______________ MAIN SITE ________________

def home(request):
    # if request.LANGUAGE_CODE !=
    persons = Person.objects.filter(status='p').order_by('name')
    projects = PortfolioProject.objects.filter(status='p').filter(featured=True)
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    total = projects.count()
    grid = 'col-lg-4 col-md-4 col-sm-12'
    return render(request, '_PT/index.html', {
        'pageName': 'docs',
        'persons': persons,
        'projects': projects,
        'docs': docs,
        'project_max': 3,
        'doc_max': 4,
        'grid': grid,
    })

def homeEN(request):
    # if request.LANGUAGE_CODE !=
    persons = Person.objects.filter(status='p').order_by('name')
    projects = PortfolioProject.objects.filter(status='p').filter(featured=True)
    docs = Doc.objects.filter(status='p').filter(language='en').order_by('-publishedDate')
    total = projects.count()
    grid = 'col-lg-4 col-md-4 col-sm-12'
    return render(request, 'EN/index.html', {
        'pageName': 'docs',
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
    return render(request, '_PT/empresa.html', {
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
    return render(request, '_PT/portfolio.html', {
        'page': 'portfolio-docs',
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
    return render(request, '_PT/portfolio.html', {
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
    return render(request, '_PT/contacto.html', {
        'pageName': 'contacto',
        'form': formClass,
        'choices': SOLICIT_CHOICES,
    })

def message(request):
    formClass = MessageForm
    return render(request, '_PT/mensagem.html', {
        'pageName': 'mensagem',
        'form': formClass,
        'choices': SOLICIT_CHOICES,
    })

def news(request, keyword='1'):
    articles = NewsObjects(keyword)

    return render(request, '_PT/news.html', {
        'page': 'news',
        'articles': articles,
        'total': len(articles),
    })








#----------- SEARCH ----------------

def searchResults(request):
    return render(request, '_PT/pesquisa.html', {
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




