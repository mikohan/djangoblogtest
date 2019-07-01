from django.shortcuts import render
from django.views import View
from elastic.documents import PostDocument




class ElasticSearchView(View):

    template_name = 'search_results.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        ordering = request.GET.get('ordering')

        search_result = PostDocument.search().sort({
            'timestamp' : {
                'order' : ordering,
                'mode'  : 'avg'
            }
        }).query('match', content=query)
        if not search_result:
            search_result = ''
        return render(request, self.template_name, {'search_result' : search_result})


