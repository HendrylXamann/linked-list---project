#Dsclp por ter saido do padrão do inglês
class Criar_usuario:
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

class Rotas:
    def __init__(self, id, prioridade, funcionario):
        self.id = id
        self.prioridade = prioridade
        self.funcionario = funcionario
        self.proximo = None
    
    def alterar_prioridade(self, nova_prioridade):
        self.prioridade = nova_prioridade
    
    def alterar_funcionario(self, novo_funcionario):
        self.funcionario = novo_funcionario

class ListaRotas:
    def __init__(self):
        self.primeira_rota = None
    
    def adicionar_rota(self, nova_rota):
        if not self.primeira_rota:
            self.primeira_rota = nova_rota
        else:
            rota_atual = self.primeira_rota
            while rota_atual.proximo:
                rota_atual = rota_atual.proximo
            rota_atual.proximo = nova_rota
    
    def remover_rota(self, id):
        rota_atual = self.primeira_rota
        rota_anterior = None

        while rota_atual:
            if rota_atual.id == id:
                if rota_anterior:
                    rota_anterior.proximo = rota_atual.proximo
                else:
                    self.primeira_rota = rota_atual.proximo
                return True
            rota_anterior = rota_atual
            rota_atual = rota_atual.proximo
        
        return False
    
    def listar_rotas(self):
        rotas = []
        rota_atual = self.primeira_rota
        while rota_atual:
            rotas.append(rota_atual)
            rota_atual = rota_atual.proximo
        return rotas
