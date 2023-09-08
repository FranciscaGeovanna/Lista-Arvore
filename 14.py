# Escreva uma função que encontre o caminho da raiz até um nó específico na árvore

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
    
    def encontrarNo(self, valor):
        c = [] # salvar caminho do nó
        if self.raiz is None:
            print("A árvore está vazia")
        elif self.encontrarNoRecursivo(self.raiz, valor, c):
            return c
        
    def encontrarNoRecursivo(self, no, valor, c):
        if no is None:
            return False
        c.append(no.valor)
        if no.valor == valor:
            return True
        if valor < no.valor:
            self.encontrarNoRecursivo(no.esquerdo, valor, c)
            return True
        elif valor > no.valor:
            self.encontrarNoRecursivo(no.direito, valor, c)
            return True
        c.pop()
        


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
    
no = int(input("\nDigite o nó que deseja encontrar o caminho: "))

if arvore.verificarValor(no):
    print("\nO caminho para esse nó é: ", arvore.encontrarNo(no))
else:
    print("\nNó não encontrado!")