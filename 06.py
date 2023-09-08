# Implemente uma função que realiza uma travessia pré-ordem (raiz-esquerda-direita) em uma árvore binária e retorna 
# os valores dos nós visitados.

class No:
    def __init__ (self, valor):
        self.valor = valor
        self.esquerdo = None
        self.direito = None
    
class Arvore:
    def __init__ (self):
        self.raiz = None
    
    def inserirEmNiveis(self, valor):
        if self.raiz is None:
           self.raiz = No(valor)
        else:
            self.inserirEmNivelRecursivo(valor, self.raiz)
    
    def inserirEmNivelRecursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerdo is None:
                no.esquerdo = No(valor)
            else:
                self.inserirEmNivelRecursivo(valor, no.esquerdo)
        else:
            if no.direito is None:
                no.direito = No(valor)
            else:
                self.inserirEmNivelRecursivo(valor, no.direito)
    
    def PreOrdem(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            self.preOrdemRecursivo(self.raiz)
    
    def preOrdemRecursivo(self, no):
        print(no.valor, end = " ")
        if no.esquerdo is not None:
            self.preOrdemRecursivo(no.esquerdo)
        if no.direito is not None:
            self.preOrdemRecursivo(no.direito)

arvore = Arvore()
arvore.inserirEmNiveis(5)
arvore.inserirEmNiveis(3)
arvore.inserirEmNiveis(7)
arvore.inserirEmNiveis(2)
arvore.inserirEmNiveis(4)
arvore.inserirEmNiveis(6)
arvore.inserirEmNiveis(8)

print("Árvore percorrida em Pré Ordem: ")
arvore.PreOrdem()