from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from django.http import Http404
from .models import Noticia, MensagemDeContato
from django.urls import reverse
from django.views.generic import FormView, TemplateView
from .forms import ContatoForm

class HomePageView(ListView):
    model = Noticia
    template_name= 'app_noticias/home.html'

def noticias_resumo(request):
    total = Noticia.objects.count()
    return render(request, 'app_noticias/resumo.html', {'total': total})


def noticias_detalhes(request, noticia_id):
    try:
        noticia = Noticia.objects.get(pk=noticia_id)
    except Noticia.DoesNotExist:
        raise Http404('Notícia não encontrada')
    return render(request, 'app_noticias/detalhes.html', {'noticia': noticia})

class ContatoView(FormView):
    template_name = 'app_noticias/contato.html'
    form_class = ContatoForm

    def form_valid(self, form):
        dados = form.clean()
        mensagem = MensagemDeContato(nome = dados['nome'], email = dados['email'], mensagem = dados['mensagem'])
        mensagem.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('sucesso')

class ContatoSucessoView(TemplateView):
    template_name = 'app_noticias/sucesso.html'

def home (request):
    return redirect ('login')

