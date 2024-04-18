import pandas as pd

def data_transform(df):
    # Convertendo a coluna 1 para datetime
    df['行维度2 row dimension 2'] = pd.to_datetime(df['行维度2 row dimension 2'])
    
    # Filtro para registros onde a coluna 1 é igual à data de hoje
    df_filtered_date = df[df['行维度2 row dimension 2'].dt.date == pd.Timestamp.today().date()]
    
    # Filtro adicional para registros onde a primeira coluna é igual a '巴西瓜卢流斯发货仓二BR_GRU_SW 2'
    # ou '圣保罗GLP中转仓Sao Paulo GLP Transit WH'
    df_filtered_warehouse = df_filtered_date[(df_filtered_date['行维度1 row dimension 1'] == '巴西瓜卢流斯发货仓二BR_GRU_SW 2') | 
                                   (df_filtered_date['行维度1 row dimension 1'] == '圣保罗GLP中转仓Sao Paulo GLP Transit WH')]
    

    df_tranformed = df_filtered_warehouse
    
    return df_tranformed

