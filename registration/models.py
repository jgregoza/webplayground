from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Mejorando el almacenamiendo de la img de avatar
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)     # OneToOneField = modelo para un perfil de usuario; un usuario un perfil
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)     # install Pillow para serivir ficheros media; en este caso imagenes
    bio = models.TextField(null=True, blank=True)   
    link = models.URLField(max_length=200, null=True, blank=True)

    # Odenara todos los objetos a partir del noombre de usuario, haciendo referencia a 'user'
    class Meta:
        ordering = ['user__username']

# Signal
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        #print("Se acaba de crear un usuario y perfil enlazado")