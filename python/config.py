from configparser import ConfigParser

def config(filename='sig.ini', section='postgresql'):
    #criando Parser do DataBase
    parser = ConfigParser()
    #lendo o file sig.ini
    parser.read(filename) 

    #pegando a seção do postgre 
    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1] 
    else:
        raise Exception('Seção {0} não foi encontrada no {1} arquivo'.format(section,filename))

    return db
