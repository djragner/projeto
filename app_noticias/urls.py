from django.urls import path

from app_noticias.views import home, noticias_detalhes, HomePageView, ContatoView, ContatoSucessoView

urlpatterns = [
    path('', home, name='login'),
    path('home/', HomePageView.as_view(), name='home'),
    path('noticia/<int:noticia_id>/', noticias_detalhes, name='detalhes'),
    path('noticia/contato/', ContatoView.as_view(), name='contato'),
    path('noticia/contato/sucesso/', ContatoSucessoView.as_view(),name='sucesso'),
]