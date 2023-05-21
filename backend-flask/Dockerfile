dockerfile# Stage 1: Prepare the app source code
FROM python:3.10-slim-buster AS builder

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN pip3 install --user -r requirements.txt

COPY . .

# Stage 2: Run the app only
FROM python:3.10-slim-buster

WORKDIR /backend-flask

RUN apt-get update && apt-get install -y --no-install-recommends curl \
  && rm -rf /var/lib/apt/lists/* 

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY external_flask.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/external_flask.sh

ENV PYTHONUNBUFFERED=1

EXPOSE ${PORT}

CMD ["/usr/local/bin/external_flask.sh"]