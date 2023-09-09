# Implemente um método na classe `Arvore` que permite a remoção de um nó específico da árvore

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
    
    def noMin(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            self.noMaxRecursivo(self.raiz)
    
    def noMinRecursivo(self, no):
        if no is None:
            return
        else:
            while no.esquerdo:
                no = no.esquerdo
            return no.valor
    
    def removerNo(self, noEscolhido):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            self.raiz = self.removerNoRecursivo(self.raiz, noEscolhido)

    def removerNoRecursivo(self, no, noEscolhido):
        if no is None:
            return None
        if noEscolhido < no.valor:
            no.esquerdo = self.removerNoRecursivo(no.esquerdo, noEscolhido)
        elif noEscolhido > no.valor:
            no.direito = self.removerNoRecursivo(no.direito, noEscolhido)
        else:
            if no.esquerdo is None:
                return no.direito
            elif no.direito is None:
                return no.esquerdo

            # Se o nó tem dois filhos
            aux = self.noMinRecursivo(no.direito)
            no.valor = aux
            no.direito = self.removerNoRecursivo(no.direito, aux)

        return no
    
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

no = int(input("\nQual nó deseja remover da árvore? "))

if arvore.verificarValor(no):
    print(f"\nO nó com o valor {no} foi removido ")
    arvore.removerNo(no)

    print("\nÁrvore atualizada:")
    arvore.emNiveis()
else:
    print(f"\nA árvore não possui um nó com valor {no}")