FROM python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*```

COPY . .

COPY external_flask.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/external_flask.sh

ENV FLASK_ENV=development

EXPOSE ${PORT}

CMD ["sh","-c","/usr/local/bin/external_flask.sh"]