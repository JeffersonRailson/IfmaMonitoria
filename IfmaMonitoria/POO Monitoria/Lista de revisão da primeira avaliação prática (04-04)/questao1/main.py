from pessoa import Pessoa, Data



p1 = Pessoa('Jefferson', 'Masculino', 1.70, 70)
dataNasci = Data(1,4,1996)
dataAtual = Data(1,4,2019)

p1.addDataNascimento(dataNasci)
p1.calcularIdade(dataAtual)

p1.mostrarDados()