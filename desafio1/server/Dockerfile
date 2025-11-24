FROM python:3.14

COPY server.py /server.py
COPY requirements.txt /requirements.txt

RUN pip install -r ./requirements.txt

EXPOSE 8080

CMD ["python", "/server.py"]