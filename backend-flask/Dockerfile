# Stage 1: Prepare the app source code
FROM python:3.10-slim-buster as builder

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN pip3 install --user -r requirements.txt

COPY . .

# Stage 2: Run the app only
FROM python:3.10-slim-buster

WORKDIR /backend-flask

COPY --from=builder /root/.local /root/.local
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY external_flask.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/external_flask.sh

ENV FLASK_ENV=development

EXPOSE ${PORT}

CMD ["sh","-c","/usr/local/bin/external_flask.sh"]