import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Importando nossa base
notas = pd.read_csv('ml-latest-small\\movies.csv')
print(notas.head())