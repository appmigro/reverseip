FROM python:3-alpine

WORKDIR /reverseip

ADD . /reverseip

EXPOSE 8000

COPY requirements.txt /reverseip/

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /reverseip

ENTRYPOINT ["python3"]

CMD ["manage.py", "runserver", "0.0.0.0:8000"]

