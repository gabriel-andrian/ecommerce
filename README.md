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
