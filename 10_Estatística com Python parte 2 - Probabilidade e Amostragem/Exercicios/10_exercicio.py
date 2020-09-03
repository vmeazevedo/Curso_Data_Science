from scipy.stats import norm

'''
Um fabricante de farinha verificou que, em uma amostra aleatória formada por 200 sacos
e 25 kg de um lote formado por 2.000 sacos, apresentou um desvio padrão amostral do peso igual a 480 g.

Considerando um erro máximo associado à média populacional igual a 0,3 kg e um nível de 
confiança igual a 95%, qual tamanho de amostra deveria ser selecionado para obtermos uma estimativa confiável do parâmetro populacional?

N = tamanho da população
z = variavel normal padronizada
sigma = desvio padrão populacional
s = desvio padrão amostral
e = erro inferencial
'''

# Obtendo N
N = 2000
print("N =",N)

# Obtendo z
z = norm.ppf((0.5 + (0.95/2)))
print("Z =",z)

# Obtendo o s
s = 480
print("s =",s)

# Obtendo o e
e = 0.3 * 1000      #convertendo kg para g
print("e =",e)

# Obtendo o n
n = ((z**2) * (s**2) * (N)) / (((z**2) * (s**2)) + ((e**2) * (N-1)))
print(n)