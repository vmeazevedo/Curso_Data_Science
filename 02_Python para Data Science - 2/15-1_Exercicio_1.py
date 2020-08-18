'''
O IMC (índice de massa corporal) é um indicador utilizado para detectar situações de obesidade ou desnutrição. 
Para obter o IMC, basta calcular a razão entre o peso de um indivíduo (kg) e sua altura elevada ao quadrado, conforme mostra a fórmula abaixo:

Considerando o enunciado acima, verifique cada alternativa e assinale as que calculam corretamente o IMC, não aprensentando erro(s) durante o seu cálculo.
'''
import numpy as np

peso = np.array([106, 68.5, 75])
altura = np.array([1.9, 1.53, 1.75])
imc = peso / altura ** 2
print(imc)