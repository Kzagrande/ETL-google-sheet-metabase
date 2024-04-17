import os 

def log(mensagem):
    env = os.getenv("PROD_ENV")
    print("O valor da variável de ambiente MINHA_VARIAVEL é:", env)
    print('log event', mensagem)
