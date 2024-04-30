class Criar_usuario():
    def __init__(self,nome,veiculo,cnh):
        self.nome = nome
        self.veiculo = veiculo
        self.cnh = cnh
        self.proximo = None #Padrão papai

    # def adicionar_usuario(self, novo_usuario):
    #     if self.proximo is None:
    #         self.proximo = novo_usuario
    #     else:
    #         self.proximo.adicionar_usuario(novo_usuario)

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

class ListaRotas:
    def __init__(self):
        self.rotas = [
            Rotas(id=1, prioridade=3, funcionario="Schopenhauer"),
            Rotas(id=2, prioridade=2, funcionario="Schopenhauer"),
            Rotas(id=3, prioridade=1, funcionario="Schopenhauer"),
            Rotas(id=4, prioridade=3, funcionario="Schopenhauer")
        ]



class Rotas():
    def __init__(self,id,prioridade,funcionario):
        self.id = id
        self.prioridade = prioridade
        self.funcionario = funcionario
        self.proximo = None 
    
    def alterar_prioridade(self, nova_prioridade):
        if nova_prioridade in (1, 2, 3):
            self.prioridade = nova_prioridade
        else:
            raise ValueError("A Prioridade deve ser 1, 2 ou 3 animal.") #validar se vou precisar pois eu que vou passar os valores
    
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

# class Adicionar_Rota:
#     """
#     Modo de uso: lista_rotas = Rotas()
#     adicionar_rota = Adicionar_Rota(lista_rotas)
#     adicionar_rota.add_nova_rota(1, 1, "João")
#     """
#     def __init__(self, lista_rotas):
#         self.lista_rotas = lista_rotas
#         self.proximo = None 

#     def add_nova_rota(self, id, prioridade, funcionario):
#         nova_rota = Rotas(id, prioridade, funcionario)
#         if self.lista_rotas.proximo is None:
#             self.lista_rotas.proximo = nova_rota
#         else:
#             self.lista_rotas.proximo.adicionar_nova_rota(nova_rota)