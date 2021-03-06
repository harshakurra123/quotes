from django.urls import path, re_path, include
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', views.index, name='index'),
    path('report/', views.coverage_repo, name='report'),
    path('about/', views.about, name='about'),
    path('docs/', views.docs, name='docs'),
    path('listpage/', views.listpage, name='listpage'),
    path('viewquotes/', views.viewquotes, name='viewquotes'),
    path('addquote/', views.get_name, name='addquote'),
    path('viewquotes/editquote/', views.editquote, name='editquote'),
    path('listpage/editquote/', views.editquote, name='editquote'),
    path('viewquotes/deletequote/', views.deletequote, name='deletequote'),
    path('listpage/deletequote/', views.deletequote, name='deletequote'),
    path('', include('social_django.urls')),
    path('logout', views.logout),
    path('reverse/', views.reverse, name='reverse'),
    path('quotecategory/', views.QuoteCategoryAPI.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]