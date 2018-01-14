"""
Written by Leo Neto
Updated on January 4, 2018
Implements a simple API with Read-Only Access

"""
from LibrariesForViews import *



class ColorListAPIView(ListAPIView):
    """
    :param None
    :return: all instances of Color ordered by project
    """
    queryset = Color.objects.all().order_by('related_project')
    serializer_class = ColorSerializer


class AudioListAPIView(ListAPIView):
    """
    :param None
    :return: all instances of Audio ordered by project
    """
    queryset = Audio.objects.all().order_by('related_project')
    serializer_class = AudioSerializer


class AudioDetailAPIView(RetrieveAPIView):
    """
    :param key: primary db key, a positive Int value representing the object's ID.
    :return: single instance of the Audio object based on db ID
    """
    queryset = Audio.objects.all().order_by('project')
    serializer_class = AudioSerializer


class AudioDetailAPIViewSlug(RetrieveAPIView):
    """
    :param slug: a string representing the object's title in URL-friendly form. Ex. french-song.
    :return: single instance of the Audio object based on slug
    """
    queryset = Audio.objects.all().order_by('project')
    serializer_class = AudioSerializer
    lookup_field = ('slug')


class DocListAPIView(ListAPIView):
    """
    :param None
    :return: all instances of Doc [provided that the objects are 'published']
    """
    queryset = Doc.objects.filter(status='p')
    serializer_class = DocSerializer


class DocDetailAPIView(RetrieveAPIView):
    """
    :param key: primary db key, a positive Int value representing the object's ID.
    :return: single instance of the Doc object [provided that the object is published]
    """
    queryset = Doc.objects.filter(status='p')
    serializer_class = DocSerializer


class DocDetailAPIViewSlug(RetrieveAPIView):
    """
    :param slug: a string representing the object's title in URL-friendly form. Ex. django-tutorial.
    :return: single instance of the Audio object based on db ID
    """
    queryset = Doc.objects.filter(status='p')
    serializer_class = DocSerializer
    lookup_field = ('slug')


class PersonListAPIView(ListAPIView):
    """
    :param None
    :return: all instances of Person [provided that the object is published]
    """
    queryset = Person.objects.filter(status='p')
    serializer_class = PersonSerializer


class PersonDetailAPIView(RetrieveAPIView):
    """
    :param key: primary db key, a positive Int value representing the object's ID.
    :return: single instance of the Audio object based on db ID
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetailAPIViewSlug(RetrieveAPIView):
    """
    :param slug: a string representing the object's name in URL-friendly form. Ex. brandon-sullivan.
    :return: single instance of the Person object based on the object's slug
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = ('slug')


class PortfolioProjectListAPIView(ListAPIView):
    """
    :param None
    :return: all instances of PortfolioProject based on db ID
    """
    queryset = PortfolioProject.objects.filter(status='p')
    serializer_class = PortfolioProjectSerializer


class PortfolioProjectDetailAPIView(RetrieveAPIView):
    """
    :param key: primary db key, a positive Int value representing the object's ID.
    :return: single instance of the PortfolioProject object based on db ID
    """
    queryset = PortfolioProject.objects.all()
    serializer_class = PortfolioProjectSerializer


class PortfolioProjectDetailAPIViewSlug(RetrieveAPIView):
    """
    :param slug: a string representing the object's name in URL-friendly form. Ex. tic-tac-toe.
    :return: single instance of the Person object based on the object's slug
    """
    queryset = PortfolioProject.objects.all()#.filter(status='p')
    serializer_class = PortfolioProjectSerializer
    lookup_field = ('slug')