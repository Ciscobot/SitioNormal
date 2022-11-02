from django.conf import settings
from django.db import models
from django.utils import timezone
#from requests import request


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

        
        
    def __str__(self):
        return self.title


class uzbekistan(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)
  

class afganistan(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
   
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class africana(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class argentina(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class austria(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class belgica(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class brunei(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class caboverde(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class canada(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class catar(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)


class corea(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class croacia(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class cuba(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class egipto(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class espana(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class etiopia(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class grecia(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class guatemala(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class hungria(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class indonesia(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class kuwait(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class lituania(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class sanmarino(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class suiza(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class turquia(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class venezuela(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class yemen(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

