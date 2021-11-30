# Tienda Virtual
En este repositorio se encuentra el trabajo para la asignatura Informática 1. Aquí se puede encontrar
* Roles de usuario
* Historias de usuario
* Diagramas ADL
* APIs backend
* Cliente frontend

## Integrantes
* Juan Camilo Sarmiento Reyes, Cod. 20152020067
* Andres RAmirez, Cod. 20161020077
* Diana Muñoz, Cod. 20212099023
* Juan Verano, Cod. 2021209026

## Ejecutar API

Crea un archivo `.env` con el siguiente formato:

```bash
MONGO_DB_NAME=my_mongo_db
MYSQL_DB_NAME=mysql_db
```

Más información del archivo [aquí](https://docs.docker.com/compose/environment-variables/)

Para levantar el API

```bash
$ docker-compose up
```

## Variables de entorno

* **MONGO_INITDB_USERNAME**: Nombre de usuario de la base de datos de mongo
* **MONGO_INITDB_PASSWORD**: Contraseña de la base de datos de mongo
* **MONGO_INITDB_DATABASE**: Nombre de la base de datos de mongo
* **MONGO_AUTHDB**: Base de datos de autenticación (colocar admin)
* **MYSQL_USERNAME**: Nombre del usuario de MySQL
* **MYSQL_PASSWORD**: Contraseña del usuario de MySQL
* **MYSQL_DATABASE**: Nombre de la base de datos de MySQL
* **MYSQL_ROOT_PASSWORD**: Contraseña del usuario de rooy de MySQL

### Lista de APIS
* Clientes
* Pedidos
* Productos

## Documentación

Para la documentación como roles de usuario, historias de usuario y ADLs [Ver el README de tienda-virtual](tienda-virtual/README.md)
