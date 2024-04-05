FROM python:3.12

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./src /src

CMD [ "kopf", "run", "/src/operator/operator.py" ]