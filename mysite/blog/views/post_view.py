from django.views import generic

# Importa o modelo Post do módulo blog.models
from blog.models import Post

# Define a classe PostView que herda de generic.ListView
class PostView(generic.ListView):
    # Define a queryset que irá buscar todos os posts com status igual a 1 (publicados)
    # e ordená-los pela data de criação em ordem decrescente
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    
    # Define o nome do template que será usado para renderizar a lista de posts
    template_name = 'index.html'

# Define a classe PostDetail que herda de generic.DetailView
class PostDetail(generic.DetailView):
    # Define o modelo que será usado para esta view, que é o modelo Post
    model = Post
    
    # Define o nome do template que será usado para renderizar os detalhes de um post específico
    template_name = 'post_detail.html'