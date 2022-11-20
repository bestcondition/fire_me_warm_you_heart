FROM python:3.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

# copy 要在 pip install 之后, 因为重建 pip install 层是费时间的
COPY . .

ENTRYPOINT ["python3", "server.py"]
