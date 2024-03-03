FROM mysql/mysql-server:latest

COPY cattle.csv /var/lib/mysql-files/

COPY init_db.sql /docker-entrypoint-initdb.d/

ENV MYSQL_ROOT_PASSWORD=asdfasdf
ENV MYSQL_DATABASE=csc468
