# -*- coding: utf-8 -*-
import numpy as np

entradas = np.array([[0, 0], [0, 1], [1, 0], [1,1]])
saidas = np.array([0, 0, 0, 1])
pesos = np.array([0.0, 0.0])
taxa_de_aprendizagem = 0.1

def step_function(soma):
    if (soma >=1):
        return 1
    return 0

def calcula_saida(registro):
    s = registro.dot(pesos)
    return step_function(s)

def treinar()
    return 0

