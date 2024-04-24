import logging
import pandas as pd
from datetime import datetime,timedelta


# Configurando o logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def transform_and_filter_data(df):
    # Renomeia as colunas do DataFrame
    column_names_mapping = {
        '行维度1 row dimension 1': 'warehouse',
        '行维度2 row dimension 2': 'day_analyzed',
        '行维度3 row dimension 3': 'total_one',
        '行维度4 row dimension 4': 'total_two',
        '行维度5 row dimension 5': 'sector',
        '数据刷新时间/当地': 'extraction_date',
        '有效效率 UPH': 'UPH',
        '有效工时 Effective Hours': 'effective_hours',
        '有效操作数 Effective Quantity': 'effective_quantity',
        '实际操作数 Real Quantity': 'real_quantity',
        'Week': 'week',
    }
    df.rename(columns=column_names_mapping, inplace=True)
    logger.info("Colunas do DataFrame renomeadas com sucesso.")

    # Filtra os dados com base na data de hoje e no nome da primeira coluna
    yesterday_date = datetime.today().date() - timedelta(days=2)
    df['day_analyzed'] = pd.to_datetime(df['day_analyzed'])
    warehouse_names = ['巴西瓜卢流斯发货仓二BR_GRU_SW 2', '圣保罗GLP中转仓Sao Paulo GLP Transit WH']
    filtered_df = df[(df['day_analyzed'].dt.date == yesterday_date) & df['warehouse'].isin(warehouse_names)]
    logger.info("Dados filtrados com base na data e nome do armazém com sucesso.")

    # Converte os tipos de dados das colunas

    filtered_df.loc[:, 'effective_hours'] = filtered_df['effective_hours'].str.replace('.', '').str.replace(',', '.').astype(float)
    filtered_df.loc[:, 'UPH'] = filtered_df['UPH'].str.replace('.', '').str.replace('.', '').str.replace(',', '.').astype(float)
    filtered_df.loc[:, 'real_quantity'] = filtered_df['real_quantity'].str.replace('.', '').str.replace(',', '.').astype(float)
    filtered_df.loc[:, 'effective_quantity'] = filtered_df['effective_quantity'].str.replace('.', '').str.replace(',', '.').astype(float)
    filtered_df['week'] = filtered_df['week'].astype(int)
    logger.info("Tipos de dados das colunas convertidos com sucesso.")


    return filtered_df

# Exemplo de uso:
# filtered_data = transform_and_filter_data(your_dataframe)
