# Implemente uma função que realiza uma travessia pós-ordem (esquerda-direita-raiz) em uma árvore binária e retorna 
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
    
    def PosOrdem(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            self.posOrdemRecursivo(self.raiz)
    
    def posOrdemRecursivo(self, no):
        if no.esquerdo is not None:
            self.posOrdemRecursivo(no.esquerdo)
        if no.direito is not None:
            self.posOrdemRecursivo(no.direito)
        print(no.valor, end = " ")

arvore = Arvore()
arvore.inserirEmNiveis(5)
arvore.inserirEmNiveis(3)
arvore.inserirEmNiveis(7)
arvore.inserirEmNiveis(2)
arvore.inserirEmNiveis(4)
arvore.inserirEmNiveis(6)
arvore.inserirEmNiveis(8)

print("Árvore percorrida em Pós Ordem: ")
arvore.PosOrdem()