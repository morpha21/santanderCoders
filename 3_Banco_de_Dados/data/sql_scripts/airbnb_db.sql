USE airbnb_db;

source /docker-entrypoint-initdb.d/sql_scripts/tables/hospede.sql;
source /docker-entrypoint-initdb.d/sql_scripts/tables/anfitriao.sql;
source /docker-entrypoint-initdb.d/sql_scripts/tables/imovel.sql;
source /docker-entrypoint-initdb.d/sql_scripts/tables/reserva.sql;
