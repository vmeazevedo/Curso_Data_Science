import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# DataFrame de exemplo
df = pd.DataFrame({
    'Sexo': ['H', 'M', 'M', 'M', 'M', 'H', 'H', 'H', 'M', 'M'],
    'Idade': [53, 72, 54, 27, 30, 40, 58, 32, 44, 51]
})
print(df)

# Media das idades
print(df['Idade'].mean())

# Media das idades por sexo
print(df.groupby(['Sexo'])['Idade'].mean())

