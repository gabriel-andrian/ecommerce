# E-COMMERCE

O objetivo desse projeto é criar um backend para um e-commerce.

## Instalação

```python
pip install -r requirements
```
## Utilização
Feito em formato de API com as seguintes rotas:

### POST /api/accounts/ **- criando um administrador**
```javascript
// REQUEST
{
	"username": "admin",
        "email": "admin@mail.com",
	"password": "1234",
	"is_superuser": true,
	"is_staff": true
}
```
**Resposta**
```javascript
// RESPONSE STATUS -> HTTP 201
{
  "id": 1,
  "is_superuser": true,
  "is_staff": true,
  "username": "admin",
  "email": "admin@mail.com"
}
```
### POST /api/login/ **- fazendo login do admin**
```javascript
// REQUEST
{
  "username": "admin",
  "email": "admin@mail.com",
  "password": "1234"
}
```
**Resposta**
```javascript
// REQUEST STATUS -> HTTP 200
{
  "token": "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```
### POST /api/product/ **- criando um novo nível no estacionamento**
```javascript
// REQUEST 
// Header -> Authorization: Token <token-do-admin>
{
	"name": "floor 1",
	"fill_priority": 2,
	"bike_spots": 1,
	"car_spots": 2
}
```
**Resposta**
```javascript
// RESPONSE STATUS -> HTTP 201
{
  "id": 1,
  "name": "floor 1",
  "fill_priority": 2,
  "available_spots": {
    "available_bike_spots": 1,
    "available_car_spots": 2
  }
}
```

### GET /api/levels/ **- listando os níveis cadastrados no estacionamento**
**Resposta**
```javascript
// RESPONSE STATUS -> HTTP 200
[
  {
    "id": 1,
    "name": "floor 1",
    "fill_priority": 5,
    "available_spots": {
      "available_bike_spots": 20,
      "available_car_spots": 50
    }
  },
  {
    "id": 2,
    "name": "floor 2",
    "fill_priority": 3,
    "available_spots": {
      "available_bike_spots": 10,
      "available_car_spots": 30
    }
  }
]
```
### POST /api/pricings/ **- criando uma nova precificação**
```javascript
// REQUEST 
// Header -> Authorization: Token <token-do-admin>
{
	"a_coefficient": 100,
	"b_coefficient": 100
}
```
**Resposta**
```javascript
// RESPONSE STATUS -> HTTP 201
{
  "id": 1,
  "a_coefficient": 100,
  "b_coefficient": 100
}
```
### POST /api/vehicles/ **- criando um novo registro de entrada**
```javascript
// REQUEST
{
	"vehicle_type": "car",
	"license_plate": "AYO1029"
}
```
**Resposta**
```javascript
// RESPONSE STATUS -> HTTP 201
{
  "id": 1,
  "license_plate": "AYO1029",
  "vehicle_type": "car",
  "arrived_at": "2021-01-25T17:16:25.727541Z",
  "paid_at": null,
  "amount_paid": null,
  "spot": {
    "id": 2,
    "variety": "car",
    "level_name": "floor 1"
  }
}
```
### PUT /api/vehicles/vehicle_id/ **- registrando a saída e pagamento do veículo**
**Resposta**
```javascript
// REPONSE STATUS -> HTTP 200
{
  "license_plate": "AYO1029",
  "vehicle_type": "car",
  "arrived_at": "2021-01-21T19:36:55.364610Z",
  "paid_at": "2021-01-21T19:37:23.016452Z",
  "amount_paid": 100,
  "spot": null
}
```
# Todo

- Model: Categories
  Fazer o post da categories junto com o Product View, usar o get_or_create()
  ex:
  band, created = Band.objects.get_or_create(
  name=request.data['name'])

          if not created:
              return Response({'message': f'{band.name} already exists'},status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        * Se ele vir com o GET é pq já existe o produto, Pode tirar o unique KEY do name do produto

loop no categories:
for tag in request.data['tags']:
tag = Tag.objects.get_or_create(\*\*tag)[0]
band.tags.add(tag)

Se já existe a categoria ele só vai pegar, se não vai criar. e add todas as categorias para o Product.

# ORDER STATUS:

fazer atualizar só o campo STATUS com as opções, se for o status CANCELADO precisa ter + 1 campo de mensagem, se não tiver retornar erro do campo faltando, os outros status podem ter mensagem == empty

# Product

Não deletar o item... Usar um state avaliable / not para saber se o item 'existe' ou não.

# Cart - Item

Quando for deletar ou encerrar o carrinho, fazer um loop pelos itens e deletar 1 por 1 (item) e no fim, deletar o carrinho.

Cart 1x1 usuario, quando o usuario fecha a compra abre uma ORDER e deleta o carrinho (Com isso vc
tem o carrinho salvo no banco de dados, mas quando o pedido é finalizado ou deletado o carrinho apaga os itens dentro.)
