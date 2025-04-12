# views.py
from rest_framework import generics
from .models import Language, Section, Header, SubHeader
from .serializers import (
    LanguageSerializer,
    SectionSerializer,
    HeaderSerializer,
    SubHeaderSerializer,
)

class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class SectionList(generics.ListCreateAPIView):
    serializer_class = SectionSerializer
    
    def get_queryset(self):
        language_id = self.kwargs['language_id']
        return Section.objects.filter(language_id=language_id)

class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class HeaderList(generics.ListCreateAPIView):
    serializer_class = HeaderSerializer
    
    def get_queryset(self):
        section_id = self.kwargs['section_id']
        return Header.objects.filter(section_id=section_id)

class HeaderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer

class SubHeaderList(generics.ListCreateAPIView):
    serializer_class = SubHeaderSerializer
    
    def get_queryset(self):
        header_id = self.kwargs['header_id']
        return SubHeader.objects.filter(header_id=header_id)

class SubHeaderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubHeader.objects.all()
    serializer_class = SubHeaderSerializer