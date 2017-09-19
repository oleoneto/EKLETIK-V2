from ViewsLibraries import *

"""

Written by Leo Neto
Updated on Sept 16, 2017

CRUD - Create Retrieve Update Delete

"""





#__________ COLOR API
class ColorListAPIView(ListAPIView):
    queryset = Color.objects.all().order_by('projectName')
    serializer_class = ColorSerializer






#___________ DOC / BLOG API

class DocListAPIView(ListAPIView):
    queryset = Doc.objects.filter(status='p')
    serializer_class = DocSerializer

class DocDetailAPIView(RetrieveAPIView):
    queryset = Doc.objects.filter(status='p')
    serializer_class = DocSerializer


class DocDetailAPIViewSlug(RetrieveAPIView):
    queryset = Doc.objects.filter(status='p')
    serializer_class = DocSerializer
    # lookup_url_kwarg = 'pk'
    lookup_field = ('slug')

class DocUpdateAPIView(UpdateAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer
    permission_classes = (IsAdminUser)

class DocDestroyAPIView(DestroyAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer







#_____________ PERSON API

class PersonListAPIView(ListAPIView):
    queryset = Person.objects.filter(status='p')
    serializer_class = PersonSerializer

class PersonDetailAPIView(RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer






#_____________ PORTFOLIO API

class PortfolioProjectListAPIView(ListAPIView):
    queryset = PortfolioProject.objects.filter(status='p')
    serializer_class = PortfolioProjectSerializer

class PortfolioProjectDetailAPIView(RetrieveAPIView):
    queryset = PortfolioProject.objects.all()
    serializer_class = PortfolioProjectSerializer