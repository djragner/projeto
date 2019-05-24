from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.nome

class Pessoa (models.Model):
    usuario = models.OneToOneField(User, on_delete = models.CASCADE,
        verbose_name = 'Usuario')
    nome = models.CharField('Nome', max_length=128)
    data_nascimento = models.DateField(
        'Data de nascimento', blank = True, null = True)
    telefone_celular = models.CharField('Telefone celular', max_length=15,
                                        help_text = 'numero do telefone celular no formato (99) 99999-9999', null = True, blank = True,
                                        )
    telefone_fixo = models.CharField('Telefone fixo', max_length=14,
                                    help_text = 'numero do telefone fixo no formato (99)9999-9999', 
                                    null = True, blank = True,
                                    )
    email = models.CharField('E-mail',max_length=128, null = True, blank = True)

    def __str__(self):
        return self.nome

 
class Noticia (models.Model):
    autor = models.ForeignKey(Pessoa, on_delete = models.CASCADE,
        verbose_name = 'Autor')
    tags = models.ManyToManyField(Tag)
    titulo = models.CharField('título ', max_length=128)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField('Data de criação: ', blank = True, null = True)
    data_pub = models.DateTimeField('Data de publicação: ', blank = True, null = True)
    publicado = models.BooleanField()

class MensagemDeContato(models.Model):
	class Meta:
		verbose_name = 'Mensagem de Contato'
		verbose_name_plural = 'Mensagenes de Contato'

	nome = models.CharField(max_length=128)
	email = models.EmailField('E-mail', null=True, blank=True)
	mensagem = models.TextField()
	data = models.DateTimeField(auto_now_add=True)
