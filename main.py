from lista import LinkedList

lista = LinkedList()
def menu():

    teclado = input( '''
     lista :
    1- Adicionar tarefa
    2- imprimir lista
    3- remover tarefa da lista
    4- atualizar tarefa

     >>>: '''
    )
    if teclado == "0": return
    if teclado == "1":
        lista.acrescentar()
    if teclado == "2":
        lista.mostrar()
    if teclado == "3":
        lista.remover()
    if teclado == "4":
        lista.atulizar()

    menu() 

menu()