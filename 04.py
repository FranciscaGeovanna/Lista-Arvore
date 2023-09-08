# Crie uma função que calcula a altura de uma árvore binária.

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
    
    def ordemEmNiveis(self):
        if self.raiz is None:
            print("A árvore está vazia")        
        else:
            print(self.raiz.valor, end = " ")
        self.ordemEmNiveisRecursivo(self.raiz)
    
    def ordemEmNiveisRecursivo(self, no):
        if no.esquerdo is not None:
            print(no.esquerdo.valor, end = " ")
        if no.direito is not None:
            print(no.direito.valor, end = " ")
        if no.esquerdo is not None:
            self.ordemEmNiveisRecursivo(no.esquerdo)
        if no.direito is not None:
            self.ordemEmNiveisRecursivo(no.direito)
    
    def altura(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            print(self.alturaRecursivo(self.raiz))
    
    def alturaRecursivo(self, no):
        if no is None:
            return 0
        
        altEsquerda = self.alturaRecursivo(no.esquerdo)
        altDireita = self.alturaRecursivo(no.direito)
        
        if altEsquerda > altDireita:
            return altEsquerda + 1
        else:
            return altDireita + 1
        
        
arvore = Arvore()
arvore.inserirEmNiveis(5)
arvore.inserirEmNiveis(3)
arvore.inserirEmNiveis(7)
arvore.inserirEmNiveis(2)
arvore.inserirEmNiveis(4)
arvore.inserirEmNiveis(6)
arvore.inserirEmNiveis(8)

print("Árvore percorrida em níveis: ")
arvore.ordemEmNiveis()
print()

print("\nAltura da árvore: ")
arvore.altura()