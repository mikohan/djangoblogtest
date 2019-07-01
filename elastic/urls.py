from django.conf.urls import url
from django.views.generic import TemplateView
from elastic.views import ElasticSearchView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='search.html'), name='elastic'),
    url(r'^elasticsearch_results$', ElasticSearchView.as_view(), name='el_res')
]
