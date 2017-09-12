"""
Serializers.py
Written by Leo Neto
Updated on Aug 25, 2017

Using the django rest framework to query, serialize, and generate views for our models.

"""
from rest_framework.serializers import ModelSerializer
from EKSite.models import *

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ('id','name','bio', 'author_bio','photo')
#end PersonSerializer

class DocSerializer(ModelSerializer):
    class Meta:
        model = Doc
        fields = ('id', 'title', 'slug', 'author', 'language', 'programmingLanguage', 'summary','content')
#end DocSerializer

class PortfolioProjectSerializer(ModelSerializer):
    class Meta:
        model = PortfolioProject
        fields = ('id', 'title', 'client', 'type', 'artwork' ,'description')

#end ProjectSerializer