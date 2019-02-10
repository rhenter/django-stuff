from django.conf.urls import include, url

from rest_framework.schemas import get_schema_view


schema_urlpatterns = [
    url(r'^v1/', include('testapp.routes', namespace='testapp')),
    url(r'', include('testapp.urls', namespace='testapp-views')),
]

schema_view = get_schema_view(
    title='test',
    patterns=schema_urlpatterns,
)

urlpatterns = [
    url(r'^/$', schema_view, name='schema')
]

urlpatterns.extend(schema_urlpatterns)
