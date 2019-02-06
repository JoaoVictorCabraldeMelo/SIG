# Projeto 1 - SIG

Projeto 1 da matéria de Sistemas de Informacão.
A premissa do projeto é criar a estrutura de entidades e atributos em um banco de dados, na forma de tabelas e colunas.  

# Instalacão

É necessária uma instalacão funcional do banco de dados [PostgreSQL](https://postgresql.org).
Para ubuntu, é possível instalar pelo próprio gerenciador de pacotes

```
$ sudo apt-get install postgresql
```

É necessário criar um banco de dados onde serão armazenados os dados. O nome pode ser o que você quiser.

```
$ createdb -U postgres <nome-banco-de-dados>
```
Exemplo:
```
$ createdb -U postgres sig
```


Para popular o banco de dados, basta rodar o servidor do postgresql (ver documentacão da sua versão instalada) e executar o script *init.sh*, passando os parâmetros do usuário e o banco de dados

```
$ ./init.sh postgres sig
```

Para realizar os cálculos basta rodar o script *calculos.sh* e passar os parâmetros de usuário do banco de dados

```
$ ./calculos.sh postgres sig
```