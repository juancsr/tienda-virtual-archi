#!/bin/bash

docker-compose up -d db

API_CLIENTES_URL=http://localhost:4000 \
API_PRODUCTOS_URL=https://productos.free.beeceptor.com \
DB_USERNAME=pedidos \
DB_PASSWORD=pedidos \
DB_NAME=pedidos \
DB_AUTH=admin \
DB_PORT=27015 \
DB_HOST=localhost \
PORT=4001 python app.py