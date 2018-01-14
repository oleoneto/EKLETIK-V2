"""
Written by Leo Neto
Updated on January 4, 2018
"""
from LibrariesForViews import *



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

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:IndexViewController'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, '_PT/registro.html', args)




def error_report(errorMessage):
    pass

def error_401(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, '401.html', {
        'origin': requestOrigin.replace("/", ""),
        'pageName': '401',
        'DocGeneralViewController': docs,
    })

def error_403(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, '403.html', {
        'origin': requestOrigin.replace("/", ""),
        'pageName': '403',
        'DocGeneralViewController': docs,
    })

def error_404(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, '404.html', {
        'origin': requestOrigin.replace("/", ""),
        'pageName': '404',
        'DocGeneralViewController': docs,
    })

def error_405(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, '405.html', {
        'origin': requestOrigin.replace("/", ""),
        'pageName': '405',
        'DocGeneralViewController': docs,
    })

def error_500(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    requestOrigin = request.get_full_path()
    return render(request, '500.html', {
        'origin': requestOrigin.replace("/", ""),
        'pageName': '500',
        'DocGeneralViewController': docs,
    })



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

def source_control(request):
    return redirect("https://github.com/ekletikstudios/")






def contact(request):
    formClass = ContactForm
    return render(request, '_PT/contact.html', {
        'pageName': 'contacto',
        'form': formClass,
        'choices': SOLICIT_CHOICES,
    })

def message(request):
    formClass = MessageForm
    return render(request, '_PT/message.html', {
        'pageName': 'mensagem',
        'form': formClass,
        'choices': SOLICIT_CHOICES,
    })

def searchResults(request):
    return render(request, '_PT/search.html', {
        'pageName': 'results',
    })