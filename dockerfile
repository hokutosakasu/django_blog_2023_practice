FROM python:3.9.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ADD . /code
RUN mkdir -p /var/run/gunicorn

CMD ["gunicorn", "django_blog.wsgi", "--bind=unix:/var/run/gunicorn/gunicorn.sock"]
