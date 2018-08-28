FROM python:3.6.3
<<<<<<< HEAD
=======
ENV MYSQL_HOST localhost
ENV MYSQL_PORT 3306
ENV MYSQL_ROOT_PASSWORD 123456
ENV MYSQL_DB admin
>>>>>>> ff01a53cea418e7a866f2b704a8f27cc25525ed3
WORKDIR /webapp
COPY . .
RUN pwd
RUN ls
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","runserver.py"]

