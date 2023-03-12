FROM python:3.11-alpine
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

ENV FILE_ROOT="/data"
ENV APP_ROOT="/myapp"

EXPOSE 5000

CMD ["python", "app.py"]

