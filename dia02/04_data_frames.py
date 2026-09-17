#%%
#Conjunto de séries - linhas e colunas 
import pandas as pd

idades = [ 
    32,38,30, 30, 31,
    35,25,29, 31, 37,
    27,23,36, 33, 39,

]

nomes = [
    "Téo", "Maria","Jose", "Luis", "Ana",
    "Paula", "João", "Pedro", "Lucas", "Marcos","Fernanda", "Carla", "Rafael", "Juliana", "Gustavo"
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)
# %%
df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = nomes

# %%
df["nomes"]

# %%
df.iloc[0]
# %%
df.iloc[0]['nomes']
# %%
df.iloc[-1]['nomes']
# %%
