FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y apache2
ENV HOSTNAME=data_input
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]