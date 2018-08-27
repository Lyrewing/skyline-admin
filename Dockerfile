FROM python:3.6.6-alpine
WORKDIR /webapp
COPY . .
RUN pwd
RUN ls
RUN python -m pip install --upgrade --force pip
RUN pip install setuptools==33.1.1
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","runserver.py"]

