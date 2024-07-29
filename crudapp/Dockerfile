FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /application

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc

COPY requirement.txt .


RUN pip install --no-cache-dir -r requirement.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["sh", "-c", "python create_db.py && uvicorn main:app --host 0.0.0.0 --port 8000"]