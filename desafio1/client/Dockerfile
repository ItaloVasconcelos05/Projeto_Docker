FROM python:3.14

COPY client.py /client.py
COPY requirements.txt /requirements.txt

RUN pip install -r ./requirements.txt

EXPOSE 8080

CMD ["python", "/client.py"]