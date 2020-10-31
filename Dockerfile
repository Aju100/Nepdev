FROM python:3.8



LABEL version="1.0"
LABEL description="Beta stage of Nepdev"

RUN mkdir /app
WORKDIR /app

RUN apt update && apt install postgresql-client -y

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .