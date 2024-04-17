import os 

def log(mensagem):
    os.getenv("PROD_ENV")
    print('log event', mensagem)
