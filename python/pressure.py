import psycopg2
from config import config 


def get_high_pressure():
    #seta a conexão    
    conn = None 

    try:
        #Faz as configurações do database
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        #Faz uma query do database 
        cur.execute("SELECT P.primeiro_nome, P.segundo_nome, P.primeiro_sobrenome FROM pessoas AS P, corpo AS C WHERE P.id = C.id AND C.sexo = 'F' AND C.tensao_arterial_diastolica < 80 AND C.tensao_arterial_sistolica < 120")

        print('A quantidade de mulheres com pressão fora do normal:', cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    get_high_pressure()
        
