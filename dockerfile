#FROM tiangolo/uwsgi-nginx-flask:python3.8
FROM singhharvin/subtraction:v1
#COPY ["./subtraction.py" ,"./uwsgi.ini", "/app/"]
COPY ["./*" , "/app/"]
