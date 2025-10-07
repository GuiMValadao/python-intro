# Mini projeto 2 - DSA fundamentos python 
# Módulo da Entidade Classe

from abc import ABC, abstractmethod

from datetime import datetime

from dsautilitarios.exceptions import SaldoInsuficienteError

class Conta(ABC):
    def __init__(self, numero: int, cliente):
        self._numero = numero
        self._saldo = 0.0
        self._cliente = cliente
        self._historico = []
        Conta._total_contas
    
    @property
    def saldo(self):
        return self._saldo
    
    @classmethod
    def get_total_contas(cls):
        return cls.get_total_contas
    
    def depositar(self, valor:float):
        if valor > 0:
            self._saldo += valor
        
            self._historico.append(datetime.now(), f"Depósito de R${valor:.2f}")
            print(f"Depósito de R&{valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")
    
    @abstractmethod
    def sacar(self, valor:float):
        pass

    def extrato(self):
        print(f"\n--- Extrato da Conta Nº {self._numero} ---")
        print(f"Cliente: {self._cliente.nome}")
        print(f"Saldo atual: R${self._saldo:.2f}")
        print("Histórico de transações:")
        if not self._historico:
            print("Nenhuma transação registrada.")
        for data, transacao in self._historico:
            print(f"- {data.strftime('%d/%m/%Y %H:%M:%S')}: {transacao}")
            print("-"*30)

class ContaCorrente(Conta):
    def 