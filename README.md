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

### POST /api/product/ **- criando um novo produto**

```javascript
// REQUEST
// Header -> Authorization: Token <token-do-seller>
{
	 "name": "Produto",
   "description": "Descrição do produto",
   "price": 9.99,
	 "categories": [
		 {
			 "name": "Categoria do Produto",
   		 "description": "Descrição da Categoria"
		 }
	 ]
}
```

**Resposta**

```javascript
// RESPONSE STATUS -> HTTP 201
{
	 "id": 1,
   "name": "Produto",
   "description": "Descrição do produto",
   "price": 9.99,
	 "categories": [
		 {
			 "id": 1,
       "name": "Categoria do Produto",
   		 "description": "Descrição da Categoria"
		 }
	 ]
}
```

### GET /api/product/ **- listando os produtos com estoque disponível**

**Resposta**

```javascript
// RESPONSE STATUS -> HTTP 200
{
	 "id": 1,
   "name": "Produto",
   "description": "Descrição do produto",
   "price": 9.99,
	 "categories": [
		 {
			 "id": 1,
       "name": "Categoria do Produto",
   		 "description": "Descrição da Categoria"
		 }
	 ]
}
```

### GET /api/product/<slug:slug>/ **- listando produto específico**

**Resposta**

```javascript
// RESPONSE STATUS -> HTTP 201
{
	 "id": 1,
   "name": "Produto",
   "description": "Descrição do produto",
   "price": 9.99,
	 "categories": [
		 {
			 "id": 1,
       "name": "Categoria do Produto",
   		 "description": "Descrição da Categoria"
		 }
	 ]
}
```

### GET /api/category/ **- listando categorias**

**Resposta**

```javascript
// RESPONSE STATUS -> HTTP 201
{
  "id": 1,
  "name": "Categoria do Produto",
  "description": "Descrição da Categoria"
}
```

### GET /api/category/<slug:slug>/ **- listando categoria específica**

**Resposta**

```javascript
// RESPONSE STATUS -> HTTP 201
{
  "id": 1,
  "name": "Categoria do Produto",
  "description": "Descrição da Categoria"
}
```

## 🛠️ Construído com

- [Django](https://www.djangoproject.com/) - O framework web usado

## ✒️ Autores

- **Gabriel Andrian** - _Atividade efetuada_ - [Gabriel Andrian](https://gitlab.com/gabriel_andrian) - [Linkedin](https://linkedin.com/in/gabriel-andrian/)
- **Paulo Santos** - _Atividade efetuada_ - [Paulo Santos](https://gitlab.com/PauloSantosIII)-[Linkedin](https://linkedin.com/in/paulosantosiii)
