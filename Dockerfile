FROM python:3.6.6-alpine
WORKDIR /webapp
RUN pwd && ls
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python","runserver.py"]

