FROM ubuntu:20.04

MAINTAINER Philipp Weiler & Maximiliam Fletzer

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y python3 pip mysql-server net-tools vim mc wget lynx curl less && apt-get clean
RUN pip install mysql-connector-python

EXPOSE 3306

ENV FOLDER_PROJECT /var/mysql_docker

RUN mkdir -p $FOLDER_PROJECT

COPY docker_run_mysql.sh $FOLDER_PROJECT
COPY start.sql $FOLDER_PROJECT
COPY ../docker_microservices/src $FOLDER_PROJECT

RUN chmod +x /var/mysql_docker/docker_run_mysql.sh

CMD ["/var/mysql_docker/docker_run_mysql.sh"]