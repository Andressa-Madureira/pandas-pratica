#%%

idades = [ 
    32,38,30, 30, 31,
    35,25,29, 31, 37,
    27,23,36, 33, 32,

]

media = sum(idades) / len(idades)
print(f'Média: {media}')

diffs = 0

for i in idades:
    diffs += (i - media) ** 2  

variancia = diffs / (len(idades) -1)

print("Variância:", variancia)


#%%
import pandas as pd

series_idades = pd.Series(idades)   
series_idades

#%%
#Estatísticas da série
media_idade = series_idades.mean()
media_idade

variancia_idade = series_idades.var()
variancia_idade

sumary = series_idades.describe()   
sumary
# %%
