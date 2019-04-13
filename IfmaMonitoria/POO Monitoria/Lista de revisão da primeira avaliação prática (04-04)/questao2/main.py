from agenda import Agenda

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
