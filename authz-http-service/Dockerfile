FROM node:16.18

ENV PORT=9002

WORKDIR /authz-http-service

COPY . /authz-http-service/
RUN npm install

EXPOSE ${PORT}

CMD ["npm", "start"]