from elevador import Elevador

e1= Elevador(50,15)
print(e1.getPessoas())
e1.inicializar(100,100)
e1.entrar(10)
e1.sair(9)
print(e1.getAndarAtual())
e1.subir(49)


print(e1.getAndarAtual())