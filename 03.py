# Implemente um método na classe `Arvore` que verifica se um valor está presente na árvore.

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
            return         
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
    
    def verificarValor(self, valor):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            return self.verificarValorRecursivo(self.raiz, valor)
    
    def verificarValorRecursivo(self, no, valor):
        if no is None:
            return False
        if no.valor == valor:
            return True
        if valor < no.valor:
            return self.verificarValorRecursivo(no.esquerdo, valor)
        else:
            return self.verificarValorRecursivo(no.direito, valor)

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

valor = int(input("\n\nDigite o valor que deseja verificar se está presente na árvore: "))
if arvore.verificarValor(valor):
    print(f"\nO valor {valor} está presente na árvore!")
else:
    print(f"\nO valor {valor} não está presente na árvore!")