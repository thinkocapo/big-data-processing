FROM python:3.7-slim

WORKDIR /app

COPY ./redis-client.py /app
COPY ./requirements.txt /app
COPY ./input_files/file-input1.csv /app
COPY ./input_files/file-input2.csv /app
COPY ./input_files/file-input3.csv /app
COPY ./input_files/file-input4.csv /app

RUN pip install -r requirements.txt

CMD ["/bin/bash"]
