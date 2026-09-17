#%%
import pandas as pd
idades = [ 
    32,38,30, 30, 31,
    35,25,29, 31, 37,
    27,23,36, 33, 39,

]

series_idade = pd.Series(idades)
series_idade


# %%
idades[-1]

# %%
series_idade[0]
idades[0]

# %%
series_idade[-1]


# %%
series_idades = series_idade.sort_values()
series_idades
# %%
series_idades[1]

# %%
#Iloc para buscar a posição atual. E não na chave associada ao indice
series_idades.iloc[-1]
# %%
series_idades.iloc[::-1]

# %%
#Setar os índices
idades = [ 
    32,38,30, 30, 31,
    35,25,29, 31, 37,
    27,23,36, 33, 39,

]

indexs = [
    "Téo", "Maria","Jose", "Luis", "Ana",
    "Paula", "João", "Pedro", "Lucas", "Marcos","Fernanda", "Carla", "Rafael", "Juliana", "Gustavo"
]

series_idades = pd.Series(idades, index=indexs)
series_idades
# %%
#Navegando nas linhas, a forma como as linhas estão ordenadas 
series_idades.iloc[0]
# %%
#Navegando pelo índice, independente da ordem das linhas
series_idades["Fernanda"]

# %%
#navegar pelo indice, podemos ocultar. loc é o default
series_idades.loc["Téo"]

# %%
