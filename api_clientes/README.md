# API Clientes

#### Obtener todos los clientes

[GET] localhost:4000/

Salida

```json
{
  "Clients": [
    {
      "address": {
        "0": "cra 1 # 1 - 1"
      },
      "city": "Bogota",
      "email": "andresramirez@gmail.com",
      "id": 0,
      "name": "Andres",
      "phone": {
        "0": "4562651",
        "1": "4578951"
      },
      "shippingQuantity": 3,
      "surname": "Ramirez"
    },
    {
      "address": {
        "0": "cra 2 # 2 - 2",
        "1": "cra 3 # 3 - 3"
      },
      "city": "Cali",
      "email": "felipehernandez@gmail.com",
      "id": 1,
      "name": "Felipe",
      "phone": {
        "number": "2131265"
      },
      "shippingQuantity": 1,
      "surname": "Hernandez"
    }
  ]
}
```

#### Obtener un cliente por ID
[GET] localhost:4000/[ID]

Salida
```json
{
  "Client": {
    "address": {
      "0": "cra 1 # 1 - 1"
    },
    "city": "Bogota",
    "email": "andresramirez@gmail.com",
    "id": 0,
    "name": "Andres",
    "phone": {
      "0": "4562651",
      "1": "4578951"
    },
    "shippingQuantity": 3,
    "surname": "Ramirez"
  },
  "message": "client found"
}
```
