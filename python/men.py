import psycopg2
from config import config

def get_men():
    
    #tenta fazer a conexão com o database
    conn = None

    try:
        #faz as configurações do database
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        #faz a query no postgre
        cur.execute("SELECT P.primeiro_nome, P.segundo_nome, P.primeiro_sobrenome FROM pessoas AS P, corpo AS C WHERE P.id = C.id AND C.sexo = 'M' AND C.altura <= 175 AND C.hemoglobina < 14.0")

        print('A quantidade de homens com altura menor que 175 e hemoglobina baixa e:', cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()
        
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None :
            conn.close()


if __name__ == "__main__":
    get_men()