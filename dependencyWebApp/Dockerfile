FROM python:3.6
ADD . /webApp
WORKDIR /webApp
EXPOSE 5000
RUN pip install flask
RUN pip install flask_sqlalchemy
RUN pip install flask_marshmallow
RUN pip install marshmallow-sqlalchemy
RUN pip install flask-security sqlalchemy
ENTRYPOINT ["python", "/app/controller.py"]

