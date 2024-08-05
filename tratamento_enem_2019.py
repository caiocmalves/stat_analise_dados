# %%
import pandas as pd
# %%

df = pd.read_csv('microdados_enem_2019_sp.csv', sep=';', encoding='iso-8859-1')
df
# %%

df.shape
# %%
df.dtypes

# %%

df1 = df.drop(columns=['CO_MUNICIPIO_RESIDENCIA'])
df1
# %%
df1.drop(columns=['CO_UF_RESIDENCIA', 'SG_UF_RESIDENCIA', 'CO_MUNICIPIO_NASCIMENTO', 'NO_MUNICIPIO_NASCIMENTO', 'CO_UF_NASCIMENTO', 'SG_UF_NASCIMENTO', 'TP_ANO_CONCLUIU', 'TP_ENSINO', 'CO_MUNICIPIO_ESC', 'CO_UF_ESC', 'SG_UF_ESC', 'TP_DEPENDENCIA_ADM_ESC', 'TP_LOCALIZACAO_ESC', 'TP_SIT_FUNC_ESC'])
# %%
#CORRIGINDO ERROS DAS NOTAS
df1.loc[:, 'NU_NOTA_CN'] /= 10
df1.loc[:, 'NU_NOTA_LC'] /= 10
df1.loc[:, 'NU_NOTA_MT'] /= 10

# %%
