from django.contrib import admin
from .models import Language, Section, Header, SubHeader

admin.site.register(Section)
admin.site.register(Language)
admin.site.register(Header)
admin.site.register(SubHeader)