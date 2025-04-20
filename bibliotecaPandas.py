import pandas as pd

venda = {'data': ['10/04/2025', '16/04/2025'],
         'valor': [500, 300],
         'produto': ['feijão', 'arroz'],
         'qtde' : [ 50, 70],
         }
vendas_df = pd.DataFrame (venda)

print (vendas_df)