
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListaPessoaView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView
from . import views


urlpatterns = [
    path('', login_required(ListaPessoaView.as_view()), name='pessoa.index'),
    path('novo/', login_required(PessoaCreateView.as_view()), name='pessoa.novo'),
    path('<int:pk>/editar', login_required(PessoaUpdateView.as_view()), name='pessoa.editar'),
    path('<int:pk>/remover', login_required(PessoaDeleteView.as_view()), name='pessoa.remover'),
    path('<int:pk_pessoa>/contatos', login_required(views.contatos), name='pessoa.contatos'),
    path('<int:pk_pessoa>/contato/novo/',login_required(views.contato_novo), name='contato.novo'),
    path('<int:pk_pessoa>/contato/<int:pk>/editar', login_required(views.contato_editar), name='contato.editar'),
    path('<int:pk_pessoa>/contato/<int:pk>/remover', login_required(views.contato_remover), name='contato.remover'),
]