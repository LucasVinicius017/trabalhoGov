from django.contrib import admin
from .models import Usuario, PontoWifi, Manutencao
# Register your models here.
admin.site.register(Usuario)
admin.site.register(PontoWifi)
admin.site.register(Manutencao)