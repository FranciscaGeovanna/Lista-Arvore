# Escreva uma função que retorna todos os nós em um determinado nível da árvore

class No:
    def __init__(self, valor):
        self.valor = valor 
        self.esquerdo = None 
        self.direito = None 
    
    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerdo and self.esquerdo.valor, self.valor, self.direito and self.direito.valor) 

class ArvoreB:
    def __init__(self):
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
    
    def emNiveis(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            print(self.raiz.valor, end = " ") 
        self.emNivelRecursivo(self.raiz) 
    
    def emNivelRecursivo(self, no):
        if no.esquerdo is not None:
            print(no.esquerdo.valor, end = " ")
        if no.direito is not None:
            print(no.direito.valor, end = " ")
        if no.esquerdo is not None:
            self.emNivelRecursivo(no.esquerdo)
        if no.direito is not None:
            self.emNivelRecursivo(no.direito)
    
    def mostrarAltura(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            print(self.alturaRecursivo(self.raiz))
    
    def altura(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            return self.alturaRecursivo(self.raiz)
    
    def alturaRecursivo(self, no):
        if no is None:
            return 0
        altEsquerda = self.alturaRecursivo(no.esquerdo)
        altDireita = self.alturaRecursivo(no.direito)
        
        if altEsquerda > altDireita:
            return altEsquerda + 1
        else:
            return altDireita + 1
    
    def nosNivel(self, nivelEscolhido):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            a = self.altura()
            if nivelEscolhido >= a:
                print(f"A árvore não possui o nível {nivelEscolhido}")
            else:
                self.nosNivelRecursivo(self.raiz, nivelEscolhido, 0)
        
    def nosNivelRecursivo(self, no, nivel, nivelEscolhido):
        if no is None:
            return None
        else:
            if nivel == 0:
                print(self.raiz.valor)
            elif nivelEscolhido == nivel:
                print(no.valor, end = ", ")
            else:
                self.nosNivelRecursivo(no.esquerdo, nivel, nivelEscolhido + 1) 
                self.nosNivelRecursivo(no.direito, nivel, nivelEscolhido + 1)

    
arvore = ArvoreB()
arvore.inserirEmNiveis(5)
arvore.inserirEmNiveis(3)
arvore.inserirEmNiveis(7)
arvore.inserirEmNiveis(2)
arvore.inserirEmNiveis(4)
arvore.inserirEmNiveis(6)
arvore.inserirEmNiveis(8)

print("Árvore inserida em níveis: ")
arvore.emNiveis()
print()
    
print("\nAltura da árvore: ")
arvore.mostrarAltura()

nivel = int(input("\nDe qual nível deseja ver os nós? "))
print(f"\nOs nós do nível {nivel} são: ", end = "")
arvore.nosNivel(nivel)