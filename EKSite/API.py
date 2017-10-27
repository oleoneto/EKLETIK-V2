from ViewsLibraries import *

"""

Written by Leo Neto
Updated on Sept 16, 2017

CRUD - Create (Post), Retrieve (Get), Update (Put) and Delete (Delete)

"""





#__________ COLOR API
# GET all instances of Color
class ColorListAPIView(ListAPIView):
    queryset = Color.objects.all().order_by('projectName')
    serializer_class = ColorSerializer




#__________ AUDIO API
# GET all instances of Color
class AudioListAPIView(ListAPIView):
    queryset = Audio.objects.all().order_by('project')
    serializer_class = AudioSerializer



#___________ DOC / BLOG API

# GET all instances of Doc
class DocListAPIView(ListAPIView):
    queryset = Doc.objects.filter(status='p')
    serializer_class = DocSerializer

# GET a single instance of Doc by id
class DocDetailAPIView(RetrieveAPIView):
    queryset = Doc.objects.filter(status='p')
    serializer_class = DocSerializer

# GET a single instance of Doc by slug
class DocDetailAPIViewSlug(RetrieveAPIView):
    queryset = Doc.objects.filter(status='p')
    serializer_class = DocSerializer
    lookup_field = ('slug')

# PUT/UPDATE a single instance of Doc
class DocUpdateAPIView(UpdateAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer
    permission_classes = (IsAdminUser)

# DELETE a single instance of Doc
class DocDestroyAPIView(DestroyAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer







#_____________ PERSON API

# GET all instances of Person
class PersonListAPIView(ListAPIView):
    queryset = Person.objects.filter(status='p')
    serializer_class = PersonSerializer

# GET a single instance of Person
class PersonDetailAPIView(RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer






#_____________ PORTFOLIO API

# GET all instances of Portfolio Project
class PortfolioProjectListAPIView(ListAPIView):
    queryset = PortfolioProject.objects.filter(status='p')
    serializer_class = PortfolioProjectSerializer

# GET a single instance of Portfolio Project
class PortfolioProjectDetailAPIView(RetrieveAPIView):
    queryset = PortfolioProject.objects.all()
    serializer_class = PortfolioProjectSerializer

class PortfolioProjectDetailAPIViewSlug(RetrieveAPIView):
    queryset = PortfolioProject.objects.all()#.filter(status='p')
    serializer_class = PortfolioProjectSerializer
    lookup_field = ('slug')