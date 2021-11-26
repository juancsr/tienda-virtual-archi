FROM node:14-alpine



WORKDIR /src/nojsapp

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm","run","dev"]