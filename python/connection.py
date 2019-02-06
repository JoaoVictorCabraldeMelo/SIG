import psycopg2
from config import config

def connect():
    #Conexão com servidor PostgreSQL
    conn = None
    try:
        #Le as conexões dos parametros 
        params = config()

        #Conetando com o PostgreSQL servidor
        conn = psycopg2.connect(**params)

        #Cria cursor para andar no banco de dados 
        cur = conn.cursor()

        #Pega a versão do banco de dados 
        print('PostgreSQL database version')
        cur.execute('SELECT version()')

        #Retorna a versão para uma variavel db_version
        db_version = cur.fetchone()
        print(db_version)

        #Termina de fechar o cursor
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None :
            conn.close()
            print('Database connection closed.')


if __name__ == "__main__":
    connect()