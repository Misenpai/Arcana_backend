from rest_framework import generics
from .models import Language, Section, Header, SubHeader
from .serializers import (
    LanguageSerializer,
    SectionSerializer,
    HeaderSerializer,
    SubHeaderSerializer,
)

class LanguageList(generics.ListCreateAPIView):
    """
    View to list all languages or create a new language.
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a specific language.
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class SectionList(generics.ListCreateAPIView):
    """
    View to list all sections or create a new section.
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a specific section.
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

# Header Views
class HeaderList(generics.ListCreateAPIView):
    """
    View to list all headers or create a new header.
    """
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer

class HeaderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a specific header.
    """
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer

# SubHeader Views
class SubHeaderList(generics.ListCreateAPIView):
    """
    View to list all subheaders or create a new subheader.
    """
    queryset = SubHeader.objects.all()
    serializer_class = SubHeaderSerializer

class SubHeaderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a specific subheader.
    """
    queryset = SubHeader.objects.all()
    serializer_class = SubHeaderSerializer