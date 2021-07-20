FROM python:3
ENV   PYTHONUNBUFFERED 1
WORKDIR /app
COPY backend/requirements.txt ./
RUN pip install -r requirements.txt
COPY backend .
EXPOSE 8000