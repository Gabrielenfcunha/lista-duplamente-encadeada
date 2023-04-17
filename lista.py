from nodo import Node

class LinkedList:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def acrescentar(self):
        nome = input('digite nome tarefa :')
        data = input('digite data :')
        descricao = input('digite descriçao:')
        novo_no = Node(nome,data,descricao)
        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            novo_no.anterior = self.fim
            novo_no.proximo = None
            self.fim.proximo = novo_no
            self.fim = novo_no

    def atulizar(self):
        valor = input('Digite o da tarefa: ') 
        data = input('digite  nova data : ')
        descricao = input('digite nva descriçao: ')
        auxiliar = self.inicio
        while auxiliar is not None:
            if auxiliar.nome == valor:
                auxiliar.nome = valor
                auxiliar.data = data
                auxiliar.descricao = descricao
            break


    def remover(self):
        nome = input('digite nome tarefa: ')
        auxiliar = self.inicio
        while auxiliar is not None:
            # se encontrar pelo nome
            if auxiliar.nome == nome:
                # se nao tiver o anterior, é o primeiro
                if auxiliar.anterior is None:
                    # a proxima passa a ser a primeira
                    self.inicio = auxiliar.proximo
                    auxiliar.proximo.anterior = None
                else:
                    # se havia algum anterior
                    auxiliar.anterior.proximo = auxiliar.proximo
                    if auxiliar.proximo is not None:
                        auxiliar.proximo.anterior = auxiliar.anterior
                break
            auxiliar = auxiliar.proximo

    def mostrar(self):
        print("Lista Duplamente Encadeada:")
        auxiliar = self.inicio
        no = ""
        while auxiliar is not None:
            if auxiliar.anterior is None:
                no += " "
            no += "|Nome: " + str(auxiliar.nome) + " Data: " + str(auxiliar.data) + " descriçao " + str(auxiliar.descricao) + " |\n "
            if auxiliar.proximo is None:
                no += " "
            auxiliar = auxiliar.proximo
        print(no)
        print("=" * 80)
