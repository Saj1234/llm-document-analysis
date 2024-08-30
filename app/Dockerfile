FROM python:3.12.1

LABEL Maintainer="Sajana.Palanagama"

WORKDIR /usr/app/src
COPY ./app ./
RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "./app.py"]