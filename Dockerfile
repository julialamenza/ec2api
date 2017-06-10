FROM jfloff/alpine-python:2.7-onbuild

WORKDIR /app

COPY . /app

EXPOSE 8080

CMD ["python", "api.py"]

