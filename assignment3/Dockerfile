FROM python:3.7-slim

# RUN mkdir p ~/test
# ADD . ~/test


WORKDIR /app
# COPY . /app
COPY ./redis-client.py /app
COPY ./requirements.txt /app
COPY ./file-input1.csv /app


# COPY file-input1.csv /app

EXPOSE 8080

RUN pip install -r requirements.txt

CMD ["/bin/bash"]
# CMD ["python", "redis-client.py", "query1", "--file", "file-input1.csv"]