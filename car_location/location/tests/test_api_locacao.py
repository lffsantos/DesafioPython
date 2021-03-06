import unittest
from car_location.location.models.categoriaveiculo import CategoriaVeiculo
from car_location.location.models.cliente import Cliente
from car_location.location.models.locacao import Locacao, LocacaoSerializer
from car_location.location.models.veiculo import Veiculo

__author__ = 'lucas'
from rest_framework import status
from django.shortcuts import resolve_url as r
from rest_framework.test import APITestCase


class LocacaoApiTests(APITestCase):

    def setUp(self):
        self.categoria = CategoriaVeiculo.objects.create(nome='Carro', tipo_cnh='B,C')
        self.veiculo = Veiculo.objects.create(modelo='Palio',
                                         categoria=self.categoria,
                                         quilometragem=55)
        self.cliente = Cliente.objects.create(nome='lucas', cpf='12345678901',
                                         tipo_cnh='B', email='lucas@test.com',
                                         phone='719991625771')

        self.data = dict(cliente=self.cliente.pk, veiculo=self.veiculo.pk,
                    data_inicial='2015-01-23', data_final='2015-01-27',
                    km_inicial=self.veiculo.quilometragem, valor=10)


    def test_new_locacao(self):
        """
        Nova locação
        """
        url = r('location:locacao-list')

        response = self.client.post(url, self.data, format='json')

        with self.subTest():
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                self.assertEqual(Locacao.objects.count(), 1)
                self.assertEqual(Veiculo.objects.get().disponivel, False)


    def test_detail_locacao(self):
        '''
        detalhe da locação
        '''
        self.muda_atributos_data(cliente=self.cliente, veiculo=self.veiculo)

        self.obj = Locacao.objects.create(**self.data)

        url = r('location:locacao-detail', self.obj.pk)

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_locacao(self):
        """
        removendo locação

        """
        self.muda_atributos_data(cliente=self.cliente, veiculo=self.veiculo)

        self.obj = Locacao.objects.create(**self.data)

        url = r('location:locacao-detail', self.obj.pk)

        response = self.client.delete(url[1:])

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_validar_cnh_invalida(self):

        url = r('location:locacao-list')
        # muda o tipo da cnh para uma invalída
        self.cliente.tipo_cnh='A'
        self.cliente.save()
        response = self.client.post(url, self.data, format='json')

        with self.subTest():
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
                self.assertEqual(response.data['code'][0], 'cnh_invalida')
                self.assertEqual(Veiculo.objects.get().disponivel, True)

    def test_locacao_mesmo_veiculo_nao_permitido(self):
        url = r('location:locacao-list')

        response = self.client.post(url, self.data, format='json')

        # coloca o veiculo indisponível
        self.veiculo.disponivel = False
        self.veiculo.save()

        response = self.client.post(url, self.data, format='json')

        with self.subTest():
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
                self.assertEqual(response.data['code'][0], 'veiculo_indisponivel')
                self.assertEqual(Veiculo.objects.get().disponivel, False)


    def muda_atributos_data(self, **kwargs):
        self.data = dict(self.data, **kwargs)
