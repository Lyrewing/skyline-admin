FROM python:3.6.3
ENV MYSQL_HOST skyline_mysql
ENV MYSQL_PORT 3306
ENV MYSQL_ROOT_PASSWORD 123456
ENV MYSQL_DB admin
ENV REDIS_HOST skyline_redis
ENV REDIS_PORT 6379
WORKDIR /webapp
COPY . .
RUN pwd
RUN ls
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","runserver.py"]

