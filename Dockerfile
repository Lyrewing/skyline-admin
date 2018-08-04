FROM python:3.6.6-alpine
RUN pip install flask
WORKDIR /webapp
COPY . .
EXPOSE 5000
CMD ["python","./app/main.py"]

