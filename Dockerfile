FROM python:3.7

COPY . /opt/test
RUN apt-get update
WORKDIR /opt/test
CMD ["pytest", "test.py"]
