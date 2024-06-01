class Criar_usuario:
    def __init__(self,nome,veiculo,cnh):
        self.nome = nome
        self.veiculo = veiculo
        self.cnh = cnh
        self.proximo = None 

    def __str__(self):
        return f'{self.nome}'

class Lista_Usuarios:
    def __init__(self):
        self.cabeca = None
        self.atual = None

    def adicionar_usuario(self, nome, veiculo, cnh):
        novo_usuario = Criar_usuario(nome, veiculo, cnh)
        if self.cabeca is None:
            self.cabeca = novo_usuario
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_usuario

    def listar_usuarios(self):
        usuarios = []
        atual = self.cabeca
        while atual is not None:
            usuarios.append(atual)
            atual = atual.proximo
        return usuarios

