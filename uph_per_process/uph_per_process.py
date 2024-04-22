import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
import json
from uph_per_process.data_extract_staff import google_sheet_extractive
from data_transform import transform_and_filter_data
from uph_per_process.data_load_staff import insert_into_database
 
def uph_per_proccess():
    try:
        # Extrair dados do Google Sheets
        df = google_sheet_extractive()
    except Exception as e:
        print("Erro ao extrair dados do Google Sheets:", e)
        return {'statusCode': 500, 'body': json.dumps({'error': 'Erro ao extrair dados do Google Sheets'})}

    try:
        # Transformar os dados
        df_filtered = transform_and_filter_data(df)
        print('df_filtered',df_filtered)
    except Exception as e:
        print("Erro ao transformar os dados:", e)
        return {'statusCode': 500, 'body': json.dumps({'error': 'Erro ao transformar os dados'})}

    try:
        # Carregar os dados transformados no banco de dados
        insert_into_database(df_filtered)
    except Exception as e:
        print("Erro ao carregar os dados no banco de dados:", e)
        return {'statusCode': 500, 'body': json.dumps({'error': 'Erro ao carregar os dados no banco de dados'})}
    

# if __name__ == "__main__":
#     # Se estiver executando diretamente, fornecer argumentos de evento e contexto
#     uph_per_proccess()
