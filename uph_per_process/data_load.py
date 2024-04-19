import logging
from sqlalchemy import event
import pandas as pd
import sqlalchemy
import pymysql
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
load_dotenv()
# Configurando o logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def insert_into_database(df):
    engine = create_engine("mysql+pymysql://" + \
                           "root" + ":" + \
                           os.getenv('DATABASE_PASS') + "@" + "localhost" + \
                           ":" + "3306" + "/" + "ware_ws_shein" + \
                           "?" + "charset=utf8mb4")

    conn = engine.connect()

    # armazenando dados no dataframe
    df = pd.DataFrame(df)
    logger.info("DataFrame criado com sucesso.")

    try:
        # inserindo dados no banco de dados
        df.to_sql("uph_per_process", conn, index=False, if_exists="append")
        logger.info("Dados inseridos no banco de dados com sucesso.")

    except Exception as e:
        logger.error(f"Erro ao inserir dados no banco de dados: {str(e)}")

    finally:
        conn.close()
        logger.info("Conexão fechada.")

# Exemplo de uso:
# insert_into_database(your_dataframe)
