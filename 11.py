# função que verifica se uma árvore binária é uma árvore de busca válida

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

    def verificarArvore(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else: 
            self.verificarArvoreRecursivo(self.raiz) 
    
    def verificarArvoreRecursivo(self, no):
        if no is None:
            return True
        if no.esquerdo is not None and no.esquerdo.valor < no.valor:
            return False
        if no.direito is not None and no.direito.valor > no.valor:
            return False
        return self.verificarArvoreRecursivo(no.esquerdo) and self.verificarArvoreRecursivo(no.direito)

        
arvore = ArvoreB()
arvore.inserirEmNiveis(5)
arvore.inserirEmNiveis(3)
arvore.inserirEmNiveis(7)
arvore.inserirEmNiveis(2)
arvore.inserirEmNiveis(4)
arvore.inserirEmNiveis(6)
arvore.inserirEmNiveis(8)

print("Árvore: ")
arvore.emNiveis()
print()
    
if arvore.verificarArvore():
    print("\nA árvore binária é uma árvore de busca válida!")
else:
    print("\nA árvore binária não é uma árvore de busca válida!")