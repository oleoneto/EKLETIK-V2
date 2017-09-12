from ViewsLibraries import *


class DocListAPIView(ListAPIView):
    queryset = Doc.objects.filter(status='p')
    serializer_class = DocSerializer

class DocDetailAPIView(RetrieveAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer

class PersonListAPIView(ListAPIView):
    queryset = Person.objects.filter(status='p')
    serializer_class = PersonSerializer

class PersonDetailAPIView(RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer



class PortfolioProjectListAPIView(ListAPIView):
    queryset = PortfolioProject.objects.filter(status='p')
    serializer_class = PortfolioProjectSerializer

class PortfolioProjectDetailAPIView(RetrieveAPIView):
    queryset = PortfolioProject.objects.all()
    serializer_class = PortfolioProjectSerializer