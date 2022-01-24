FROM python:3.8
MAINTAINER Joe Cates "jcates5@uoregon.edu"
RUN apt-get update -y
COPY . /app
WORKDIR /app
RUN python -m pip install -U pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
