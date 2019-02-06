-- tabela de auditores
select distinct
	nome_auditor,
	profissao_auditor
into auditores
from raw_data;

-- tabela de pacientes
select distinct
	id,
	atendimentos_mes,
	nome_auditor,
	primeiro_nome,
	segundo_nome,
	primeiro_sobrenome,
	segundo_sobrenome,
	rg,
	(current_date - data_nascimento)/365 as idade,
	(current_date - data_entrada)/365 as tempo_entrada
into pessoas
from raw_data;

alter table pessoas
add primary key (id);

-- tabela de informacão corporal
select distinct
	id,
	sexo,
	peso,
	altura,
	tensao_arterial_sistolica,
	tensao_arterial_diastolica,
	hemodialisis,
	dosis_dialisis,
	hemoglobina,
	albumina_serica,
	fosforo
into corpo
from raw_data;

alter table corpo
add constraint infofk foreign key (id)
references pessoas (id);
