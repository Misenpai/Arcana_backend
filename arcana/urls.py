# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('languages/', views.LanguageList.as_view(), name='language-list'),
    path('languages/<int:pk>/', views.LanguageDetail.as_view(), name='language-detail'),
    path('languages/<int:language_id>/sections/', views.SectionList.as_view(), name='section-list'),
    path('sections/<int:section_id>/headers/', views.HeaderList.as_view(), name='header-list'),
    path('headers/<int:header_id>/subheaders/', views.SubHeaderList.as_view(), name='subheader-list'),
]