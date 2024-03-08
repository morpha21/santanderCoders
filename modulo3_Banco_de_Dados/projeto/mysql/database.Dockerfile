FROM mysql
COPY ./chessdatabase.sql /docker-entrypoint-initdb.d/

ENTRYPOINT ["docker-entrypoint.sh"]
