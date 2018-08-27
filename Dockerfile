FROM python:3.6.3
WORKDIR /webapp
COPY . .
RUN pwd
RUN ls
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","runserver.py"]

