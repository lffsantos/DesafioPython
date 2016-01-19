from car_location.location.models.categoriaveiculo import CategoriaVeiculo, \
    CategoriaVeiculoSerializer
from car_location.location.models.cliente import Cliente
from car_location.location.models.cliente import ClienteSerializer
from car_location.location.models.devolucao import Devolucao, \
    DevolucaoSerializer
from car_location.location.models.locacao import Locacao, LocacaoSerializer
from car_location.location.models.veiculo import Veiculo
from car_location.location.models.veiculo import VeiculoSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

__author__ = 'lucas'

@authentication_classes((BasicAuthentication,))
@permission_classes((IsAuthenticated,))
class CategoriaVeiculoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaVeiculo.objects.all()
    serializer_class = CategoriaVeiculoSerializer

@authentication_classes((BasicAuthentication,))
@permission_classes((IsAuthenticated,))
class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

@authentication_classes((BasicAuthentication,))
@permission_classes((IsAuthenticated,))
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

@authentication_classes((BasicAuthentication,))
@permission_classes((IsAuthenticated,))
class LocacaoViewSet(viewsets.ModelViewSet):
    queryset = Locacao.objects.all()
    serializer_class = LocacaoSerializer

@authentication_classes((BasicAuthentication,))
@permission_classes((IsAuthenticated,))
class DevolucaoViewSet(viewsets.ModelViewSet):
    queryset = Devolucao.objects.all()
    serializer_class = DevolucaoSerializer

