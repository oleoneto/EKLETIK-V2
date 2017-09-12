from ModelsLibraries import *





###_______________________________________
# This is a generic site-wide person class
# All FIELDS are REQUIRED
# Names are limited to 45 characters
# Using Uploads/profiles/ for profile pictures
# bio should be a short description of the person
# Persons can be marked as published or drafted as needed...
# __str__ returns the value of name in a given instance of Person
class Person(models.Model):
    name = models.CharField(max_length=45, blank=False)
    photo = models.ImageField(upload_to="Uploads/profiles/", max_length=45, blank=False)
    position = models.CharField(max_length=45, blank=True)
    board_member = models.BooleanField(default=False)
    bio = models.TextField(max_length=100, blank=False)
    author_bio = models.TextField(max_length=550, blank=True)
    github_username = models.CharField(max_length=30, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')

    class Meta:
        verbose_name_plural = "Team Members"

    def __str__(self):
        return self.name










#
# A class to manage portfolio projects
# Variables are self-explanatory
class PortfolioProject(models.Model):
    title = models.CharField(max_length=15, blank=False)
    type = models.CharField(max_length=15, blank=False)
    author = models.ForeignKey(Person)
    client = models.CharField(max_length=15, blank=False)
    description = models.TextField()
    details = models.CharField(max_length=30, blank=True)
    artwork = models.ImageField(upload_to='Uploads/projects/', max_length=45, blank=False)
    featured = models.BooleanField(default=False)
    publishedDate = models.DateTimeField(auto_now=False)
    slug = models.SlugField(max_length=50, unique=True, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')

    class Meta:
        verbose_name_plural = 'Portfolio Projects'

    def __str__(self):
        return self.title

    def get_author(self):
        return self.author.name

#end Project








#
# A single class that stores HEX color information
# This class can be featured alongside Project
# When alongside Project, multiple instances of Color can be created in the admin panel.
class Color(models.Model):
    projectName = models.ForeignKey(PortfolioProject)
    hexColor = models.CharField(max_length=7)

    def __str__(self):
        return self.hexColor
#end Color







#
# Similar to Color, Photo can be featured alongside Project.
# Multiple instances of Photo can also be created in the admin panel.
class Photo(models.Model):
    projectName = models.ForeignKey(PortfolioProject)
    photo = models.ImageField(upload_to='uploads/projects/', max_length=45)
#end Photo


















###
# A class for the documentation on the site.
# This can be used for blog posts as well
# Author is a reference to an instance of Person
# Title must be less than 45 characters
# Content can be as long as it needs to be
# publication date should be auto generated
# Update date should also be auto generated, but no one should be able to change it.
# get_author returns the name of the instance of Person who authored the doc.
# __str__ returns the value of title inside an instance of Docs.
###

class Doc(models.Model):
    author = models.ForeignKey(Person)
    title = models.CharField(max_length=45, blank=False)
    content = models.TextField(blank=False)
    summary = models.TextField(blank=True, max_length=100)
    publishedDate = models.DateField(default=date.today)
    updatedDate = models.DateTimeField(auto_now=True)
    programmingLanguage = models.CharField(max_length=5, choices=TOPICS, default='py')
    language = models.CharField(max_length=2, choices=IDIOMAS, default='pt')
    slug = models.SlugField(max_length=50, unique=True, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')

    class Meta:
        verbose_name_plural = 'Docs'

    def get_author(self):
        return self.author.name

    def get_programmingLanguage(self):
        return self.programmingLanguage

    def __str__(self):
        return self.title



class FeaturedHeader(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField(max_length=140, blank=True)
    emoji = models.BooleanField(default=False)
    link = models.URLField(default='https://ekletik.com')
    photo_link = models.URLField(blank=False)
    photo = models.ImageField(upload_to='uploads/featured/', max_length=45, blank=True)

    class Meta:
        verbose_name = 'Featured Header'
        verbose_name_plural = 'Site Headers'

    def __str__(self):
        return self.title