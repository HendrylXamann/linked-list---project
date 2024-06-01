import datetime

class Noh:
    def __init__(self, rota, funcionario, prioridade):
        self.rota = rota
        self.funcionario = funcionario
        self.prioridade = prioridade
        self.esquerda = None
        self.direita = None
        self.deletado = False
        self.duplicatas = []

class Arvore:
    def __init__(self):
        self.raiz = None
        self.nos = {} 

    def inserir(self, rota, funcionario, prioridade):
        novo_noh = Noh(rota, funcionario, prioridade)
        self.nos[rota] = novo_noh
        if self.raiz is None:
            self.raiz = novo_noh
        else:
            self._inserir(self.raiz, novo_noh)

    def _inserir(self, noh, novo_noh):
        if int(novo_noh.prioridade) < int(noh.prioridade):
            if noh.esquerda is None:
                noh.esquerda = novo_noh
            else:
                self._inserir(noh.esquerda, novo_noh)
        else:
            if noh.direita is None:
                noh.direita = novo_noh
            else:
                self._inserir(noh.direita, novo_noh)

    def delete(self, rota):
        self.raiz = self._delete(self.raiz, rota)

    """Plus 1
    simples(basico)
    def _delete(self, noh, rota):
        if noh is None:
            return noh

        if rota < noh.rota:
            noh.esquerda = self._delete(noh.esquerda, rota)
        elif rota > noh.rota:
            noh.direita = self._delete(noh.direita, rota)
        else:
            if noh.esquerda is None:
                return noh.direita
            elif noh.direita is None:
                return noh.esquerda

            temp = self._menorValorNoh(noh.direita)
            noh.rota = temp.rota
            noh.funcionario = temp.funcionario
            noh.prioridade = temp.prioridade
            noh.direita = self._delete(noh.direita, temp.rota)
        return noh
    """
    
    def _delete(self, noh, rota):
        if noh is None:
            return noh

        if rota < noh.rota:
            noh.esquerda = self._delete(noh.esquerda, rota)
        elif rota > noh.rota:
            noh.direita = self._delete(noh.direita, rota)
        else:
            if noh.deletado:
                return noh

            if noh.duplicatas:
                duplicata = noh.duplicatas.pop()
                noh.rota = duplicata.rota
                noh.funcionario = duplicata.funcionario
                noh.prioridade = duplicata.prioridade
            else:
                noh.deletado = True
                noh.timestamp_delecao = datetime.datetime.now()
                if noh.esquerda is None:
                    return noh.direita
                elif noh.direita is None:
                    return noh.esquerda

                temp = self._menorValorNoh(noh.direita)
                noh.rota = temp.rota
                noh.funcionario = temp.funcionario
                noh.prioridade = temp.prioridade
                noh.direita = self._delete(noh.direita, temp.rota)

        return noh

    def _menorValorNoh(self, noh):
        atual = noh
        while(atual.esquerda is not None):
            atual = atual.esquerda
        return atual

    def busca(self, rota):
        return self._busca(self.raiz, rota)

    def _busca(self, noh, rota):
        if noh is None or noh.rota == rota:
            return noh
        if noh.rota < rota:
            return self._busca(noh.direita, rota)
        return self._busca(noh.esquerda, rota)
    
    #Plus 2
    def listar_rotas(self):
        rotas = self._listar_rotas(self.raiz)
        return sorted(rotas, key=lambda rota: rota[2])
    """simples(basico)
    def listar_rotas(self):
        rotas = self._listar_rotas(self.raiz, [])
        return sorted(rotas, key=lambda rota: rota[2])

    def _listar_rotas(self, noh, rotas):
        if noh:
            self._listar_rotas(noh.esquerda, rotas)
            rotas.append((noh.rota, noh.funcionario, noh.prioridade))
            self._listar_rotas(noh.direita, rotas)
        return rotas
    """
    def _listar_rotas(self, raiz):
        rotas = []
        pilha = []
        noh_atual = raiz
        while True:
            while noh_atual is not None:
                pilha.append(noh_atual)
                noh_atual = noh_atual.esquerda
            if pilha:
                noh_atual = pilha.pop()
                rotas.append((noh_atual.rota, noh_atual.funcionario, noh_atual.prioridade))
                noh_atual = noh_atual.direita
            else:
                break
        return rotas
    
    def inserir_por_prioridade(self, rota, funcionario, prioridade):
        novo_noh = Noh(rota, funcionario, prioridade)
        if self.raiz is None:
            self.raiz = novo_noh
        else:
            self._inserir_por_prioridade(self.raiz, novo_noh)

    def _inserir_por_prioridade(self, noh, novo_noh):
        if novo_noh.prioridade < noh.prioridade:
            if noh.esquerda is None:
                noh.esquerda = novo_noh
            else:
                self._inserir_por_prioridade(noh.esquerda, novo_noh)
        else:
            if noh.direita is None:
                noh.direita = novo_noh
            else:
                self._inserir_por_prioridade(noh.direita, novo_noh)
    
    def alterar_prioridade(self, rota_id, nova_prioridade):
        noh = self.nos.get(rota_id)
        if noh:
            print(f"A rota {rota_id} terá prioridade: {nova_prioridade}")
            noh.prioridade = nova_prioridade  

    def alterar_funcionario(self, rota_id, novo_funcionario):
        noh = self.nos.get(rota_id) 
        if noh:
            print(f"A rota  {rota_id} terá o funcionário: {novo_funcionario}")
            noh.funcionario = novo_funcionario


