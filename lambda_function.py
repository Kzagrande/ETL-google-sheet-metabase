import json
from data_extract import google_sheet_extractive
from data_transform import data_transform  # Importe a função data_transform
 
def lambda_handler(event, context):
    # Executar a função google_sheet_extractive
    df = google_sheet_extractive()

    # Executar a função data_transform e passar o resultado de google_sheet_extractive como parâmetro
    df_filtered = data_transform(df)
    print('df_filtered',df_filtered)
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }

# if __name__ == "__main__":
#     # Se você estiver executando o lambda_handler diretamente, precisa fornecer argumentos de evento e contexto
#     lambda_handler(event=None, context=None)
