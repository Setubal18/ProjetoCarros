from django.shortcuts import render
from .models import Proprietario,Veiculo,Acessorio
# Create your views here.
def listar_veiculo(request, template_name="veiculos_list.html"):
   veiculo = Veiculo.objects.all()
   veiculos = {'lista': veiculo}
   return render(request, template_name, veiculos)