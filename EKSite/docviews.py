from ViewsLibraries import *
from .models import *



def docs(request):
    docs = Doc.objects.filter(status='p').filter(language='pt').order_by('-publishedDate')
    return render(request, '_PT/docs.html', {
        'page': 'doc-docs',
        'docs': docs,
        'doc_max': 100,
    })


def singleDoc(request, key):
    if 'gs' in key:
        relateddocs = Doc.objects.filter(status='p').order_by('-publishedDate')
    else:
        relateddocs = Doc.objects.filter(status='p').order_by('-publishedDate').filter(language='pt')

    try:
        doc = Doc.objects.get(slug=key)
        authorID = doc.author_id
        authorTotal = Doc.objects.filter(author=authorID).filter(status='p').count()
    except Doc.DoesNotExist:
        raise Http404('404 - Doc not found', {'pageName': '404'})

    return render(request, '_PT/docs.html', {
        'page': 'doc-single',
        'doc': doc,
        'title': doc.title,
        'content': doc.content,
        'author': doc.get_author(),
        'authorSlug': doc.author.get_slug(),
        'authorID': doc.author_id,
        'authorPhoto': doc.author.photo.url,
        'authorGithub': doc.author.github_username,
        'authorBio': doc.author.author_bio,
        'authorTotal': authorTotal,
        'language': doc.get_programmingLanguage_display(),
        'date': doc.publishedDate,
        'id': doc.id,
        'relateddocs': relateddocs,
    })


def authorDoc(request, key):
    try:
        author = Person.objects.get(slug=key)
        docs = Doc.objects.filter(author__slug=key).order_by('-publishedDate').filter(status='p')
    except Doc.DoesNotExist:
        raise Http404('Author has no docs')
    return render(request, '_PT/docs.html', {
        'page': 'doc-author',
        'docs': docs,
        'author': author,
        'authorPhoto': author.photo.url,
        'authorBio': author.author_bio,
        'authorGithub': author.github_username,
    })


def django(request):
    key = "gswd"
    authordocs = Doc.objects.filter(author__name=key).filter(status='p')
    relateddocs = Doc.objects.filter(status='p').order_by('-publishedDate')
    try:
        doc = Doc.objects.get(slug=key)
    except Doc.DoesNotExist:
        raise Http404('Doc 404')
    return render(request, '_PT/docs.html', {
        'page': 'doc-single',
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
    return render(request, '_EN/docs.html', {
        'docs': docs,
    })