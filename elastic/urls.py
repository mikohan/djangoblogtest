from django.conf.urls import url
from django.views.generic import TemplateView
from elastic.views import ElasticSearchView

from .views import HomeView, ProductView, FacetedSearchView, autocomplete

urlpatterns = [
    url(r'^post/$', TemplateView.as_view(template_name='search.html'), name='post'),
    url(r'^elasticsearch_results$', ElasticSearchView.as_view(), name='el_res'),
    url(r'^$', HomeView.as_view()),
    url(r'^product/(?P<slug>[\w-]+)/$', ProductView.as_view(), name='product'),
    url(r'^search/autocomplete/$', autocomplete),
    url(r'^find/', FacetedSearchView.as_view(), name='haystack_search'),
]

urlpatterns += [

]
