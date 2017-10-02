"""
Serializers.py
Written by Leo Neto
Updated on Aug 25, 2017

Using the django rest framework to query, serialize, and generate views for our models.

"""
from rest_framework.serializers import ModelSerializer
from EKSite.models import *


class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = ('projectTitle','hexColor',)


class DocSerializer(ModelSerializer):
    class Meta:
        model = Doc
        fields = ('id', 'uri', 'title', 'slug', 'writer', 'language', 'sintax', 'summary','content')
#end DocSerializer



class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ('id','name','bio', 'author_bio','photo')
#end PersonSerializer



class PortfolioProjectSerializer(ModelSerializer):
    class Meta:
        model = PortfolioProject
        fields = ('id', 'uri', 'title', 'client', 'type', 'artwork', 'description')

#end ProjectSerializer