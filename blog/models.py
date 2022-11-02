from django.conf import settings
from django.db import models
from django.utils import timezone
from requests import request


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
    fotos = models.ImageField(upload_to = 'Fotos/uzbekistan', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/uzbekistan', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/uzbekistan', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/uzbekistan', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/uzbekistan', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/uzbekistan', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/uzbekistan', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/uzbekistan', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/uzbekistan', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/uzbekistan', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/uzbekistan', blank = True)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)
  

class afganistan(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/afganistan', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/afganistan', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/afganistan', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/afganistan', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/afganistan', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/afganistan', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/afganistan', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/afganistan', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/afganistan', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/afganistan', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/afganistan', blank = True)
   
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class africana(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/africana', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/africana', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/africana', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/africana', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/africana', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/africana', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/africana', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/africana', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/africana', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/africana', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/africana', blank = True)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class argentina(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/argentina', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/argentina', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/argentina', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/argentina', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/argentina', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/argentina', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/argentina', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/argentina', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/argentina', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/argentina', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/argentina', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class austria(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/austria', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/austria', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/austria', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/austria', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/austria', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/austria', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/austria', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/austria', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/austria', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/austria', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/austria', blank = True)
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class belgica(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/belgica', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/belgica', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/belgica', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/belgica', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/belgica', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/belgica', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/belgica', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/belgica', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/belgica', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/belgica', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/belgica', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class brunei(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/brunei', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/brunei', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/brunei', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/brunei', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/brunei', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/brunei', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/brunei', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/brunei', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/brunei', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/brunei', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/brunei', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class caboverde(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/caboverde', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/caboverde', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/caboverde', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/caboverde', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/caboverde', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/caboverde', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/caboverde', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/caboverde', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/caboverde', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/caboverde', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/caboverde', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class canada(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/canada', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/canada', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/canada', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/canada', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/canada', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/canada', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/canada', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/canada', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/canada', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/canada', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/canada', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class catar(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/catar', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/catar', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/catar', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/catar', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/catar', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/catar', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/catar', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/catar', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/catar', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/catar', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/catar', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)


class corea(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/corea', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/corea', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/corea', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/corea', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/corea', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/corea', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/corea', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/corea', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/corea', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/corea', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/corea', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class croacia(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/croacia', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/croacia', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/croacia', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/croacia', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/croacia', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/croacia', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/croacia', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/croacia', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/croacia', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/croacia', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/croacia', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class cuba(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/cuba', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/cuba', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/cuba', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/cuba', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/cuba', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/cuba', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/cuba', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/cuba', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/cuba', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/cuba', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/cuba', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class egipto(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/egipto', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/egipto', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/egipto', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/egipto', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/egipto', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/egipto', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/egipto', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/egipto', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/egipto', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/egipto', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/egipto', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class espana(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/espana', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/espana', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/espana', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/espana', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/espana', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/espana', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/espana', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/espana', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/espana', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/espana', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/espana', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class etiopia(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/etiopia', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/etiopia', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/etiopia', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/etiopia', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/etiopia', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/etiopia', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/etiopia', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/etiopia', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/etiopia', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/etiopia', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/etiopia', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class grecia(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/grecia', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/grecia', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/grecia', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/grecia', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/grecia', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/grecia', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/grecia', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/grecia', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/grecia', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/grecia', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/grecia', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class guatemala(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/guatemala', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/guatemala', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/guatemala', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/guatemala', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/guatemala', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/guatemala', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/guatemala', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/guatemala', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/guatemala', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/guatemala', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/guatemala', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class hungria(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/hungria', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/hungria', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/hungria', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/hungria', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/hungria', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/hungria', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/hungria', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/hungria', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/hungria', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/hungria', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/hungria', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class indonesia(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/indonesia', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/indonesia', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/indonesia', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/indonesia', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/indonesia', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/indonesia', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/indonesia', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/indonesia', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/indonesia', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/indonesia', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/indonesia', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class kuwait(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/kuwait', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/kuwait', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/kuwait', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/kuwait', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/kuwait', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/kuwait', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/kuwait', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/kuwait', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/kuwait', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/kuwait', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/kuwait', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class lituania(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/lituania', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/lituania', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/lituania', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/lituania', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/lituania', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/lituania', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/lituania', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/lituania', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/lituania', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/lituania', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/lituania', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class sanmarino(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/sanmarino', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/sanmarino', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/sanmarino', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/sanmarino', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/sanmarino', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/sanmarino', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/sanmarino', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/sanmarino', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/sanmarino', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/sanmarino', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/sanmarino', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class suiza(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/suiza', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/suiza', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/suiza', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/suiza', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/suiza', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/suiza', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/suiza', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/suiza', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/suiza', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/suiza', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/suiza', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class turquia(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/turquia', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/turquia', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/turquia', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/turquia', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/turquia', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/turquia', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/turquia', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/turquia', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/turquia', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/turquia', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/turquia', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class venezuela(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/venezuela', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/venezuela', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/venezuela', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/venezuela', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/venezuela', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/venezuela', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/venezuela', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/venezuela', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/venezuela', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/venezuela', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/venezuela', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

class yemen(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotos = models.ImageField(upload_to = 'Fotos/yemen', blank = True)
    fotos1 = models.ImageField(upload_to = 'Fotos/yemen', blank = True)
    fotos2 = models.ImageField(upload_to = 'Fotos/yemen', blank = True)
    fotos3 = models.ImageField(upload_to = 'Fotos/yemen', blank = True)
    fotos4 = models.ImageField(upload_to = 'Fotos/yemen', blank = True)
    fotos5 = models.ImageField(upload_to = 'Fotos/yemen', blank = True)
    fotos6 = models.ImageField(upload_to = 'Fotos/yemen', blank = True)
    fotos7 = models.ImageField(upload_to = 'Fotos/yemen', blank = True)
    fotos8 = models.ImageField(upload_to = 'Fotos/yemen', blank = True)
    fotos9 = models.ImageField(upload_to = 'Fotos/yemen', blank = True)
    fotos10 = models.ImageField(upload_to = 'Fotos/yemen', blank = True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.texto)

