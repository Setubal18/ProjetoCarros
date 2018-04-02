from django.contrib import admin
from .models import Proprietario,Veiculo,Acessorio

# Register your models here.

admin.site.register(Proprietario)
admin.site.register(Veiculo)
admin.site.register(Acessorio)