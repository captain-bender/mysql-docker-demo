FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=passwd
ENV MYSQL_DATABASE=classicmodels

COPY ./mysqlsampledatabase.sql /docker-entrypoint-initdb.d/