class Criar_usuario():
    def __init__(self,nome,veiculo,cnh):
        self.nome = nome
        self.veiculo = veiculo
        self.cnh = cnh
        self.proximo = None #Padrão papai

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

class ListaRotas:
    def __init__(self):
        self.rotas = [
            Rotas(id=1, prioridade=3, funcionario="Schopenhauer"),
            Rotas(id=2, prioridade=2, funcionario="Schopenhauer"),
            Rotas(id=3, prioridade=1, funcionario="Schopenhauer"),
            Rotas(id=4, prioridade=3, funcionario="Schopenhauer")
        ]

class Rotas():
    def __init__(self,id=None, prioridade=None, funcionario=None):
        self.id = id
        self.prioridade = prioridade
        self.funcionario = funcionario
        self.proximo = None 
    
    def alterar_prioridade(self, nova_prioridade):
        if nova_prioridade in (1, 2, 3):
            self.prioridade = nova_prioridade
    
    def alterar_funcionario(self, novo_func):
        self.funcionario = novo_func

    def excluir_rota(self):
        """
        A próxima rota vai continuar apontando para o próximo elemento da lista;
        """
        if self.proximo is not None:
            self.proximo.excluir_rota()
        else:
            pass

