#importando os campos de usuário padrão do django
from django.contrib.auth.models import User

#importando o post_save pois a action esperada para disparar o sinal é a criação(save) de um novo usuário 
from django.db.models.signals import post_save
from django.shortcuts import redirect


#sender -> modelo que é observado(User)
#instance -> objeto que é observado(neste caso o usuário)
#created -> indica que o objeto foi criado retornando true. Caso seja modificado ou deletado retorna false

def cadastroPerfil(sender, instance, created, **kwargs):
    if created:
        if not hasattr(instance, "user_profile"):
            redirect('/perfil/')

post_save.connect(cadastroPerfil, sender=User)