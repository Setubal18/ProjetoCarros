from django.shortcuts import render
from .models import Veiculo


# Create your views here.
# Listar todos os veiculos
# def listar_veiculo(request):
#     veiculo = Veiculo.objects.all()
#     veiculos = {'lista': veiculo}
#     return render(request, 'veiculos_list.html', veiculos)

# listar veiculos por pesquisa
def listar_veiculo(request):
    query = request.GET.get("busca", '')
    if query:
        veiculo = Veiculo.objects.filter(modelo__icontains=query)
    else:
      veiculo = Veiculo.objects.all()
    veiculos = {'lista': veiculo}
    return render(request, 'veiculos_list.html', veiculos)