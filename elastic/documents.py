from django_elasticsearch_dsl import DocType, Index
from elastic.models import Post

post = Index('posts')

@post.doc_type
class PostDocument(DocType):


    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'timestamp'
        ]