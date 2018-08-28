FROM python:3.6.3
ENV MYSQL_HOST db
ENV MYSQL_PORT 3306
ENV MYSQL_ROOT_PASSWORD 123456
ENV MYSQL_DB admin
WORKDIR /webapp
COPY . .
RUN pwd
RUN ls
RUN pip install -r requirements.txt
EXPOSE 5000
#CMD ["python","runserver.py"]

