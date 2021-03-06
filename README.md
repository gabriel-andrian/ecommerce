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
