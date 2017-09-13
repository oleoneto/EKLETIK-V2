from ViewsLibraries import *
from .models import *





def home(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    return render(request, 'PT/docs.html', {
        'docs': docs,
    })

def singleDoc(request, key):
    authordocs = Doc.objects.filter(author__name=key).filter(status='p').filter(language='pt')
    relateddocs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    try:
        doc = Doc.objects.get(slug=key)
    except Doc.DoesNotExist:
        raise Http404('Doc 404')
    return render(request, 'PT/doc-single.html', {
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




def django(request):
    key = "getting-started-django"
    authordocs = Doc.objects.filter(author__name=key).filter(status='p')
    relateddocs = Doc.objects.filter(status='p').order_by('-publishedDate')
    try:
        doc = Doc.objects.get(slug=key)
        if not doc:
            key = "getting-started-django"
            doc = Doc.objects.get(slug=key)
            if not doc:
                key = "django"
                doc = Doc.objects.get(slug=key)
    except Doc.DoesNotExist:
        raise Http404('Doc 404')
    return render(request, 'PT/doc-single.html', {
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




def homeEN(request):
    docs = Doc.objects.filter(status='p').filter(language='en').order_by('-publishedDate')
    return render(request, 'EN/docSingle.html', {
        'docs': docs,
    })