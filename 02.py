# Crie uma classe "Arvore" para inserir um novo valor em um nó de uma árvore binária.

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
    
def inserirNos():
    arvore = Arvore()
    
    quant = int(input("Quantos nós deseja inserir na árvore? "))
    for i in range(quant):
        nos = input(f"Digite o valor do {i+1}° nó: ")
        arvore.inserirEmNiveis(nos)
    print("\nSua árvore inserida em níveis: ")
    arvore.ordemEmNiveis()
    
    return arvore

Arvore = inserirNos()