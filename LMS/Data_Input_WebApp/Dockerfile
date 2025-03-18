FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y apache2
RUN rm /var/www/html/index.html
ENV HOSTNAME=data_input_webapp
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]