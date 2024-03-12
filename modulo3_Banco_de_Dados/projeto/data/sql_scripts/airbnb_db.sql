USE airbnb_db;

source /docker-entrypoint-initdb.d/sql_scripts/tables/hospede.sql;
source /docker-entrypoint-initdb.d/sql_scripts/tables/acompanhante.sql;
source /docker-entrypoint-initdb.d/sql_scripts/tables/anfitriao.sql;
source /docker-entrypoint-initdb.d/sql_scripts/tables/imoveis.sql;
source /docker-entrypoint-initdb.d/sql_scripts/tables/reserva.sql;
