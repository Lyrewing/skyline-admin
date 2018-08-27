FROM python:3.6.6-alpine
WORKDIR /webapp
COPY . .
RUN pwd
RUN ls
RUN easy_install -U setuptools
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","runserver.py"]

