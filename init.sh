#!/bin/bash

# Lê as entradas de um arquivo csv e separa os dados
# em tabelas, previamente selecionadas pela análise
# de entidades e atributos.

USER=$1
DATABASE=$2

# Criacão da tabela raw_data
psql -U $USER -d $DATABASE -f sql/raw_data.sql

# Copiar os dados do csv para a pasta
psql -U $USER -d $DATABASE -c "\copy raw_data from 'csv/dados.csv' delimiter ','"

# Popular as tabelas permanentes
psql -U $USER -d $DATABASE -f sql/entities.sql

# Deleta a tabela raw data
psql -U $USER -d $DATABASE -c "drop table raw_data;"
