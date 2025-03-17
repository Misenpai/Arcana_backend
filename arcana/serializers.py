from rest_framework import serializers
from .models import Language, Section, Header, SubHeader

class SubHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubHeader
        fields = ['id', 'title', 'content', 'code']

class HeaderSerializer(serializers.ModelSerializer):
    subheaders = SubHeaderSerializer(many=True, read_only=True)

    class Meta:
        model = Header
        fields = ['id', 'title', 'subheaders']

class SectionSerializer(serializers.ModelSerializer):
    headers = HeaderSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['id', 'title', 'headers']

class LanguageSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Language
        fields = ['id', 'name', 'description', 'sections', 'link'] 