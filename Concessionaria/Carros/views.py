from django.shortcuts import render
from .models import Veiculo


# Create your views here.
def listar_veiculo(request, ):
    veiculo = Veiculo.objects.all()
    veiculos = {'lista': veiculo}
    return render(request, 'veiculos_list.html', veiculos)
