FROM python:3.11.7-slim

ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . .


EXPOSE 8000

CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]