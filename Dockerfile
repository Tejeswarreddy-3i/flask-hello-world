FROM python:3

WORKDIR /usr/src/

COPY Src/application.py .
COPY Src/requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./application.py"]
