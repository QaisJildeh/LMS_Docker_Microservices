FROM mcr.microsoft.com/mssql/server:2019-latest
ENV ACCEPT_EULA=Y \
    SA_PASSWORD=yourStrong(!)Password \
    MSSQL_PID=Express
ENV HOSTNAME=mySQL
EXPOSE 1433
CMD ["/opt/mssql/bin/sqlservr"]