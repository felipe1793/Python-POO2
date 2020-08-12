# Nome: Felipe de Santana Gonçalves RA:1901648
 

from abc import ABC, abstractmethod

class Parte(ABC):
    codigo = int
    nome = str
    descricao = str
    valor = float

    def __init__(self, codigo, nome, descricao, valor):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

    @abstractmethod
    def calcular_valor(self):
        return self.valor

    @abstractmethod
    def exibir(self):
        print('codigo....:', self.codigo)
        print('nome....:', self.nome)
        print('descrição....:', self.descricao)
        print('valor....:', self.valor)

    def get_valor(self):
        return self.valor


class Motor(Parte):
    potencia = float
    corrente = float
    rpm = int

    def __init__(self, codigo, nome, descricao, valor, potencia, corrente, rpm):
        super().__init__(codigo, nome, descricao, valor)
        self.potencia = potencia
        self.corrente = corrente
        self.rpm = rpm

    def calcular_valor(self):
        return self.valor

    def exibir(self):
        print('codigo....:', self.codigo)
        print('nome....:', self.nome)
        print('descrição....:', self.descricao)
        print('valor....:', self.valor)
        print('potencia...:', self.potencia)
        print('corrente...:', self.corrente)
        print('rpm...:', self.rpm)


class Parafuso(Parte):
    comprimento = float
    diametro = float

    def __init__(self, codigo, nome, descricao, valor, comprimento, diametro):
        super().__init__(codigo, nome, descricao, valor)
        self.comprimento = comprimento
        self.diametro = diametro

    def calcular_valor(self):
        return self.valor

    def exibir(self):
        print('codigo....:', self.codigo)
        print('nome....:', self.nome)
        print('descrição....:', self.descricao)
        print('valor....:', self.valor)
        print('comprimento...:', self.comprimento)
        print('diametro...:', self.diametro)


class Item():
    quantidade = int

    def __init__(self, referencia_ao_objeto_parte, quantidade):
        self.referencia_ao_objeto_parte = referencia_ao_objeto_parte
        self.quantidade = quantidade

    def calcular_valor(self):
        return self.quantidade * self.referencia_ao_objeto_parte.get_valor() 
