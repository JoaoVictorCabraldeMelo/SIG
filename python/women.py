import psycopg2
from config import config

def get_women():

    #Tenta fazer a conexão com database do PostgreSQL
    conn = None     

    try:
        #Faz as configuração do database 
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        #Faz uma query no database
        cur.execute("SELECT P.primeiro_nome, P.segundo_nome, P.primeiro_sobrenome FROM pessoas AS P, corpo AS C WHERE P.id = C.id AND C.sexo = 'F' AND C.altura <= 150 ")
        
        print('A quantidade de mulheres com altura menor que 150 : ', cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()
        
        cur.close()

    except (Exception , psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    get_women()