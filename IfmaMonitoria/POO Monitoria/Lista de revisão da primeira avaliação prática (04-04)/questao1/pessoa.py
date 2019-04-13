class Pessoa:
    def __init__(self,nome, genero, altura, peso):
        self.__nome = nome
        self.__genero = genero
        self.__altura = altura
        self.__peso = peso
        self.__dataNascimento = None
        self.__idade = None
    
    def getNome(self):
        return self.__nome
    
    def getGenero(self):
        return self.__genero
    
    def getAltura(self):
        return self.__altura
    
    def getPeso(self):
        return self.__peso
    
    def getDataNascimento(self):
        return self.__dataNascimento
    
    def getIdade(self):
        return self.__idade
    
    def setNome(self, nome):
        self.__nome = nome
    
    def setGenero(self, genero):
        self.__genero = genero
    
    def setAltura(self, altura):
        self.__altura = altura
    
    def setPeso(self, peso):
        self.__peso = peso
    
    def setDataNascimento(self, dataNasc):
        self.__dataNascimento = dataNasc
    
    def setIdade(self, idade):
        self.__idade = idade

    def addDataNascimento(self, obgData):
        self.__dataNascimento = obgData

    def calcularIdade(self, dataAtual):
        if dataAtual.dia >= self.__dataNascimento.dia and dataAtual.mes >= self.__dataNascimento.mes:
            self.__idade = dataAtual.ano - self.__dataNascimento.ano 
        elif dataAtual.dia < self.__dataNascimento.dia and dataAtual.mes <= self.__dataNascimento.mes:
            self.__idade = (dataAtual.ano - self.__dataNascimento.ano) - 1
        elif dataAtual.mes < self.__dataNascimento.mes:
            self.__idade = (dataAtual.ano - self.__dataNascimento.ano) - 1

    def mostrarDados(self):
        print('-' *50)
        print(f'nome: {self.__nome}'f'\nGenero: {self.__genero}'f'\nAltura: {self.__altura}'f'\nPeso: {self.__peso}'f'\nData de Nascimento: {self.__dataNascimento.dia}/{self.__dataNascimento.mes}/{self.__dataNascimento.ano}'f'\nIdade: {self.__idade}')
        print('-' *50)

class Data:
    def __init__(self,dia, mes, ano ):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    
    











