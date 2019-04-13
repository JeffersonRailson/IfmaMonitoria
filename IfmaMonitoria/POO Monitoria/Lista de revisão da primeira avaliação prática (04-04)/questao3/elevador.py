class Elevador:
    def __init__ (self,totalAndares, capacidade):
        self.__tolAndares= totalAndares
        self.__capacidadePessoas = capacidade
        self.__andarAtual= 50
        self.__pessoas= 0
    
    def getTotalAndades(self):
        return self.__tolAndares

    def getCapacidadePessoas(self):
        return self.__capacidadePessoas

    def getAndarAtual(self):
        return self.__andarAtual

    def getPessoas(self):
        return self.__pessoas

    
    def setTotalAndades(self, total):
        self.__tolAndares = total

    def setCapacidadePessoas(self, capacidadePessoas):
        self.__capacidadePessoas = capacidadePessoas

    def setAndarAtual(self, andaAtual):
        self.__andarAtual = andaAtual

    def setPessoas(self, pessoas):
        self.__pessoas = pessoas

    def entrar(self,numPessoas):
        if self.__capacidadePessoas - self.__pessoas >= numPessoas:
            self.__pessoas += numPessoas 
    
    def sair(self,numPessoas):
        if self.__pessoas >= numPessoas:
            self.__pessoas -= numPessoas
    
    def subir(self,andaUp):
        if self.__tolAndares - self.__andarAtual >= andaUp:
            self.__andarAtual += andaUp
        elif self.__tolAndares - self.__andarAtual < andaUp:
            self.__andarAtual = self.__tolAndares
    
    def decer(self,andaDawn):
        if self.__andarAtual >= andaDawn:
            self.__andarAtual -= andaDawn
        elif self.__andarAtual < andaDawn:
            self.__andarAtual = 0
    
    def inicializar(self,capacidade, totalAndaders):
        self.setCapacidadePessoas(capacidade)
        self.setTotalAndades(totalAndaders)
        self.__andarAtual= 0