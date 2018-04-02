from .models import Veiculo
from django.shortcuts import render
from django.core import paginator
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator


# Create your views here.
# Listar todos os veiculos
# def listar_veiculo(request):
#     veiculo = Veiculo.objects.all()
#     veiculos = {'lista': veiculo}
#     return render(request, 'veiculos_list.html', veiculos)

# listar veiculos por pesquisa

# def listar_veiculo(request):
#     query = request.GET.get("busca", '')
#     if query:
#         veiculo = Veiculo.objects.filter(modelo__icontains=query)
#     else:
#       veiculo = Veiculo.objects.all()
#     veiculos = {'lista': veiculo}
#     return render(request, 'veiculos_list.html', veiculos)

# Organizar
# def listar_veiculo(request):
#     query = request.GET.get("busca", '')
#     ordenar = request.GET.get("ordenar", '')
#
#     if query:
#         veiculo = Veiculo.objects.filter(modelo__icontains=query)
#     else:
#
#         if ordenar:
#             veiculo = Veiculo.objects.all().order_by(ordenar)
#
#         else:
#             veiculo = Veiculo.objects.all()
#     veiculos = {'lista': veiculo}
#     return render(request, 'veiculos_list.html', veiculos)

#Paginacao
def listar_veiculo(request):
     query = request.GET.get("busca", '')
     page = request.GET.get('page', '')
     ordenar = request.GET.get("ordenar", '')
     if query:
         veiculo = Veiculo.objects.filter(modelo__icontains=query)
     else:
         try:
             if ordenar:
                 veiculo = Veiculo.objects.all().order_by(ordenar)
             else:
                 veiculo = Veiculo.objects.all()
             veiculo = Paginator(veiculo, 1)
             veiculo = veiculo.page(page)
         except PageNotAnInteger:
             veiculo = veiculo.page(1)
         except EmptyPage:
             veiculo = paginator.page(paginator.num_pages)
     veiculos = {'lista': veiculo}
     return render(request, 'veiculos_list.html', veiculos)