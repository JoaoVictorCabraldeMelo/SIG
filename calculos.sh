#!/bin/bash

# Cálculo de média, variância e desvio padrão para
# todas as colunas quantitáveis do banco de dados

USER=$1
DATABASE=$2

rm resultados/*.txt

for filename in sql/calculos/*.sql; do
	newname=${filename%.sql}
	realname=${newname##*/}
	printf "\n=== %s === \n\n" "${realname^^}"
	while IFS=, read -r tabela coluna; do
		psql -U $USER -f $filename -v tabela=$tabela -v coluna=$coluna $DATABASE | \
		awk -v coluna="${coluna}" '/[0-9]{5}/ {printf "%s: %.6f\n", coluna, $1}' | \
		tee -a resultados/$realname.txt
	done < csv/colunas.csv
done  