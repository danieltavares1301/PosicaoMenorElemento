from random import*

# elemento inicializando com id e peso
class Elemento:
    def __init__(self, id, peso):
        self.id = id
        self.peso = peso

class Lista:
    def __init__(self):
        self.elementos = []

#funçao para adicionar um objeto Elemento na lista
    def addElemento(self, id, peso):
        self.elementos.append(Elemento(id, peso))

#função que percorre a lista de elementos e mostra todos os elementos contidos nela
    def mostrarElementos(self):
        for i in self.elementos:
            print("elemento: ",i.id, "- peso: ",i.peso)

    def menorPeso(self):
        # menor inicialmente como infinito
        menor = float("inf")
        posicao = 0
        for i in self.elementos: #percorrendo a lista
            if i.peso < menor:   # se o peso do elemento for menor que menor(infinito)
                menor = i.peso   # menor terá o valor do peso do elemento 
                posicao = self.elementos.index(i) #posicao receberá a posição do menor
        print("o elemento que está na posição",
              posicao, "tem o menor peso que é ",
              menor)
         
class main:
    e = Lista()
    # inseri 150 elementos e seus pesos aleatórios entre 0 e 2000 para demonstrar a função
    for i in range(150):
        for j in range(1):
            j = randint(0,2000)
            e.addElemento(i,j)
    e.menorPeso()
    e.mostrarElementos()
                
