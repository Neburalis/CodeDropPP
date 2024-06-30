FROM python:3.12.3-slim
LABEL authors="arseniy"

RUN apt-get update \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000