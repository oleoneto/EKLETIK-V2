from ModelsLibraries import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save




#_________________________________________
# This is a generic site-wide person class
# All FIELDS are REQUIRED except the author_bio
# Names are limited to 45 characters
# Using Uploads/profiles/ for profile pictures
# bio should be a short description of the person
# Persons can be marked as published or drafted as needed...
# __str__ returns the value of name in a given instance of Person
class Person(models.Model):
    name = models.CharField(max_length=45, blank=False)
    photo = models.ImageField(upload_to="uploads/profiles/", max_length=45, blank=False)
    position = models.CharField(max_length=45, blank=True)
    board_member = models.BooleanField(default=False)
    bio = models.TextField(max_length=100, blank=False)
    author_bio = models.TextField(max_length=550, blank=True)
    github_username = models.CharField(max_length=30, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    slug = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "Team Members"

    def get_slug(self):
        name = self.name.lower()
        name = name.replace(" ", "-")
        return name

    def __str__(self):
        return self.name










#_____________________________________
# A class to manage portfolio projects
# Variables are self-explanatory
class PortfolioProject(models.Model):
    title = models.CharField(max_length=30, blank=False)
    type = models.CharField(max_length=15, blank=False)
    author = models.ForeignKey(Person)
    client = models.CharField(max_length=15, blank=False)
    description = models.TextField()
    details = models.CharField(max_length=30, blank=True)
    artwork = models.ImageField(upload_to='uploads/projects/', max_length=45, blank=False)
    featured = models.BooleanField(default=False)
    publishedDate = models.DateTimeField(auto_now=False)
    slug = models.SlugField(max_length=50, unique=True, blank=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')

    class Meta:
        verbose_name_plural = 'Portfolio Projects'

    def __str__(self):
        return self.title

    def uri(self):
        return reverse('project', args=[str(self.slug)])

    def get_author(self):
        return self.author.name

#end Project








#_________________________________________________
# A single class that stores HEX color information
# This class can be featured alongside Project
# When alongside Project, multiple instances of Color can be created in the admin panel.
class Color(models.Model):
    projectName = models.ForeignKey(PortfolioProject)
    hexColor = models.CharField(max_length=7)

    def projectTitle(self):
        return self.projectName.title

    def hex(self):
        return self.hexColor

    def __str__(self):
        return self.hexColor
#end Color




#__________________________________________
# Similar to Color, Photo can be featured alongside Project.
# Multiple instances of Photo can also be created in the admin panel.
class Photo(models.Model):
    projectName = models.ForeignKey(PortfolioProject)
    photo = models.ImageField(upload_to='uploads/projects/', max_length=45)

    def projectTitle(self):
        return self.projectName.title
#end Photo



#___________________________________________
class Audio(models.Model):
    project = models.ForeignKey(PortfolioProject)
    source = models.FileField(upload_to='uploads/audios/', max_length=60)
    number = models.IntegerField(blank=True)
    title = models.CharField(max_length=50, blank=False)
    artist = models.CharField(max_length=50, blank=False)
    composer = models.CharField(max_length=50, blank=True)
    genre = models.CharField(max_length=15, blank=True)
    slug = models.SlugField(max_length=50, blank=True)

    def related_project(self):
        return self.project.title

    def set_slug(self):
        slug = self.title.lower().replace(" ", "-")

    def get_slug(self):
        slug = self.title.lower().replace(" ", "-")
        return slug

    #def uri(self):
    #    return self.source

    def __str__(self):
        return self.title
#end Audio



#__________________________________________
# A class for the documentation on the site.
# This can be used for blog posts as well
# Author is a reference to an instance of Person
# Title must be less than 45 characters
# Content can be as long as it needs to be
# publication date should be auto generated
# Update date should also be auto generated, but no one should be able to change it.
# get_author returns the name of the instance of Person who authored the doc.
# __str__ returns the value of title inside an instance of Docs.
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
        verbose_name_plural = 'Documentation & Blog'

    def writer(self):
        return self.author.name

    def get_author(self):
        return self.author.name

    def sintax(self):
        return self.get_programmingLanguage_display()

    def uri(self):
        return reverse('doc', args=[str(self.slug)])

    def __str__(self):
        return self.title
#end Doc



#________________________
# Removed Featured Header
#________________________


class Message(models.Model):
    sender  = models.EmailField()
    subject = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    origin = models.CharField(max_length=200)

    def summary(self):
        return "Message about {} from {}".format(self.subject, self.sender)

    def __str__(self):
        return self.subject
#end Message





#_________________________

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='London')

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)

    london = UserProfileManager()

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)