FROM python:3.6.6-alpine
RUN pip install flask &&\
    pip install tornado

WORKDIR /webapp
COPY . .
EXPOSE 5000
CMD ["python","runserver.py"]

