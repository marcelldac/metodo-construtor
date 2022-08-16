#metodo construtor

class cachorro:
    def __init__(self, nome):
        #ações a ser realizadas assim que o objeto for criado // antes mesmo da interação do usuário
        #criação de uma variável interna
        self.nome = nome
        print('seu cachorro se chama', self.nome )

nome_cachorro = input('Digite o nome de seu cachorro: ')
objeto = cachorro(nome_cachorro)