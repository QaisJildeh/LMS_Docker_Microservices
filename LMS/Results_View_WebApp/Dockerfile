FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y apache2
ENV HOSTNAME=results_view
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]