class Noh:
    def __init__(self, rota, funcionario, prioridade):
        self.rota = rota
        self.funcionario = funcionario
        self.prioridade = prioridade
        self.esquerda = None
        self.direita = None

class ArvoreBiBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, rota, funcionario, prioridade):
        novo_noh = Noh(rota, funcionario, prioridade)
        if self.raiz is None:
            self.raiz = novo_noh
        else:
            self._inserir(self.raiz, novo_noh)

    def _inserir(self, noh, novo_noh):
        if novo_noh.prioridade < noh.prioridade:
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

    def _menorValorNoh(self, noh):
        current = noh
        while(current.esquerda is not None):
            current = current.esquerda
        return current

    def busca(self, rota):
        return self._busca(self.raiz, rota)

    def _busca(self, noh, rota):
        if noh is None or noh.rota == rota:
            return noh
        if noh.rota < rota:
            return self._busca(noh.direita, rota)
        return self._busca(noh.esquerda, rota)
    
    def listar_rotas(self):
        return self._listar_rotas(self.raiz, [])

    def _listar_rotas(self, noh, rotas):
        if noh:
            self._listar_rotas(noh.esquerda, rotas)
            rotas.append((noh.rota, noh.funcionario, noh.prioridade))
            self._listar_rotas(noh.direita, rotas)
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
        noh = self.busca(rota_id)
        if noh:
            print(f"Alterando prioridade da rota {rota_id} para {nova_prioridade}")
            self.delete(rota_id)
            self.inserir_por_prioridade(noh.rota, noh.funcionario, nova_prioridade)

    def alterar_funcionario(self, rota_id, novo_funcionario):
        noh = self.busca(rota_id)
        if noh:
            print(f"Alterando funcionário da rota {rota_id} para {novo_funcionario}")
            noh.funcionario = novo_funcionario