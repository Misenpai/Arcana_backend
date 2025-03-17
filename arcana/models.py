from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True, null=True) 
    def __str__(self):
        return self.name

class Section(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Header(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='headers')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class SubHeader(models.Model):
    header = models.ForeignKey(Header, on_delete=models.CASCADE, related_name='subheaders')
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    code = models.TextField(blank=True)

    def __str__(self):
        return self.title