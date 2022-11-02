from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *
from .forms import PostForm

def vista_inicio(request):
    #vista_inicio = get_object_or_404
    return render(request, 'blog/base.html', {})

def vista_mañana(request):
    #vista_mañana = get_object_or_404
    return render(request, 'blog/turnos/mañana.html', {})

def vista_tarde(request):
    #vista_tarde = get_object_or_404
    return render(request, 'blog/turnos/tarde.html', {})

def vista_Suiza(request):
    vista_Suiza = suiza.objects.all()  #get_object_or_404
    return render(request, 'blog/paises/Suiza.html', {"texto" : vista_Suiza})

def vista_uzbekistan(request):
    vista_uzbekistan = uzbekistan.objects.all() #get_object_or_404
    return render(request, 'blog/paises/Uzbekistán.html', {"texto" : vista_uzbekistan})

def vista_afganistan(request):
    vista_afganistan = afganistan.objects.all() #get_object_or_404
    return render(request, 'blog/paises/Afganistán.html', { "texto" : vista_afganistan})

def vista_belgica(request):
    vista_belgica = belgica.objects.all() #get_object_or_404
    return render(request, 'blog/paises/Bélgica.html', {"texto" : vista_belgica})

def vista_españa(request):
    vista_españa = espana.objects.all() #get_object_or_404
    return render(request, 'blog/paises/España.html', {"texto" : vista_españa})

def vista_cuba(request):
    vista_cuba = cuba.objects.all() #get_object_or_404
    return render(request, 'blog/paises/Cuba.html', {"texto" : vista_cuba})

def vista_kuwait(request):
    vista_kuwait = kuwait.objects.all() #get_object_or_404
    return render(request, 'blog/paises/Kuwait.html', {"texto" : vista_kuwait})

def vista_indonesia(request):
    vista_indonesia = indonesia.objects.all() #get_object_or_404
    return render(request, 'blog/paises/Indonesia.html', {"texto" : vista_indonesia})

def vista_grecia(request):
    vista_grecia = grecia.objects.all() #get_object_or_404
    return render(request, 'blog/paises/Grecia.html', {"texto" : vista_grecia})

def vista_lituania(request):
    vista_lituania = lituania.objects.all() #get_object_or_404
    return render(request, 'blog/paises/Lituania.html', {"texto": vista_lituania})

def vista_yemen(request):
    vista_yemen = yemen.objects.all() #get_object_or_404
    return render(request, 'blog/paises/Yemen.html', {"texto" : vista_yemen})

def vista_austria(request):
    vista_austria = austria.objects.all() #get_object_or_404
    return render(request, 'blog/paises/Austria.html', {"texto" : vista_austria})

def vista_egipto(request):
    vista_egipto = egipto.objects.all() #get_object_or_404
    return render(request, 'blog/paises/Egipto.html', {"texto" : vista_egipto})

def vista_africana(request):
    vista_africana = africana.objects.all() #get_object_or_404
    return render(request, 'blog/paises/Africana.html', {"texto" : vista_africana})

def vista_brunei(request):
    vista_brunei = brunei.objects.all() #get_object_or_404
    return render(request, 'blog/paises/brunei.html', {"texto" : vista_brunei})

def vista_guatemala(request):
    vista_guatemala = guatemala.objects.all() #get_object_or_404
    return render(request, 'blog/paises/guatemala.html', {"texto" : vista_guatemala}) 

def vista_croacia(request):
    vista_croacia = croacia.objects.all() #get_object_or_404
    return render(request, 'blog/paises/croacia.html', {"texto" : vista_croacia})

def vista_catar(request):
    vista_catar = catar.objects.all() #get_object_or_404
    return render(request, 'blog/paises/catar.html', {"texto" : vista_catar})

def vista_turquia(request):
    vista_turquia = turquia.objects.all() #get_object_or_404
    return render(request, 'blog/paises/turquia.html', {"texto" : vista_turquia})

def vista_cabo(request):
    vista_cabo = caboverde.objects.all() #get_object_or_404
    return render(request, 'blog/paises/cabo.html', {"texto" : vista_cabo})

def vista_hungria(request):
    vista_hungria = hungria.objects.all() #get_object_or_404
    return render(request, 'blog/paises/hungria.html', {"texto" : vista_hungria})

def vista_venezuela(request):
    vista_venezuela = venezuela.objects.all() #get_object_or_404
    return render(request, 'blog/paises/venezuela.html', {"texto" : vista_venezuela})

def vista_coreadelsur(request):
    vista_coreadelsur = corea.objects.all() #get_object_or_404
    return render(request, 'blog/paises/coreadelsur.html', {"texto" : vista_coreadelsur})

def vista_argentina(request):
    vista_argentina = argentina.objects.all() #get_object_or_404
    return render(request, 'blog/paises/argentina.html', {"texto" : vista_argentina})

def vista_marino(request):
    vista_marino = sanmarino.objects.all() #get_object_or_404
    return render(request, 'blog/paises/marino.html', {"texto" : vista_marino})

def vista_etiopia(request):
    vista_etiopia = etiopia.objects.all() #get_object_or_404
    return render(request, 'blog/paises/etiopia.html', {"texto" : vista_etiopia})

def vista_canada(request):
    vista_canada = canada.objects.all() #get_object_or_404
    return render(request, 'blog/paises/canada.html', {"texto" : vista_canada})
# Create your views here.
