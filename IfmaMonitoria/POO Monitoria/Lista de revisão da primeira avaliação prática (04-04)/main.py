# -*- coding: UTF-8 -*-
from questao1.pessoa  import Pessoa, Data
from questao2.agenda import Agenda
from questao3.elevador import Elevador



# Questão 01


print('-'*50)
print("Questão 01")
p1 = Pessoa('Jefferson', 'Masculino', 1.70, 70)
dataNasci = Data(1,4,1996)
dataAtual = Data(1,4,2019)

p1.addDataNascimento(dataNasci)
p1.calcularIdade(dataAtual)

p1.mostrarDados()

# Quetão 02
print("Questão 02")
print('-'*50)

a1 = Agenda()
a1.armazenaPessoa('jefferson', 23, 1.7)
a1.armazenaPessoa('b', 23, 1.7)
a1.armazenaPessoa('c', 23, 1.7)
a1.armazenaPessoa('jefferson', 23, 1.7)
a1.armazenaPessoa('b', 23, 1.7)
a1.armazenaPessoa('c', 23, 1.7)
a1.armazenaPessoa('jefferson', 23, 1.7)
a1.armazenaPessoa('b', 23, 1.7)
a1.armazenaPessoa('c', 23, 1.7)
a1.armazenaPessoa('c', 23, 1.7)
a1.armazenaPessoa('c', 23, 1.7)


a1.imprimirAgenda()
a1.imprimirPessoa(1)
a1.removerPessoa('jefferson')
a1.imprimirAgenda()

# Questão 03
print('-'*50)

print("Questão 03")

print('-'*50)

e1= Elevador(50,15)
print(e1.getPessoas())
e1.inicializar(100,100)
e1.entrar(10)
e1.sair(9)
print(e1.getAndarAtual())
e1.subir(49)


print(e1.getAndarAtual())
