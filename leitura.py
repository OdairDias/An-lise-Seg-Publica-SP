import pandas as pd
# definindo variaveis
furto_celulares= ('dados_furto_celulares.csv')
roubo_celulares= ('dados_roubo_celulares.csv')
#definindo funções
df_furto_celulares= pd.read_csv(furto_celulares,encoding='utf-8', sep = ';')
df_roubo_celulares= pd.read_csv(furto_celulares,encoding='utf-8', sep = ';')

#df_furto_celulares.head(5)
#df_roubo_celulares.head(5)

print(df_roubo_celulares)
print(df_furto_celulares)
marge=pd.concat([df_furto_celulares,df_roubo_celulares])
marge.to_csv('furtos_roubos')



