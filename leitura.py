import pandas as pd
import matplotlib

furto_celulares= ('dados_furto_celulares.csv')
df_furto_celulares= pd.read_csv(furto_celulares,encoding='utf-8', sep = ';')

df_furto_celulares.head(5)
print(df_furto_celulares)

