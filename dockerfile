FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ["./subtraction.py" ,"./uwsgi.ini", "/app/"]
