FROM python:3.11
COPY app.py /app.py
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
EXPOSE 5001
CMD ["python", "/app.py"]
