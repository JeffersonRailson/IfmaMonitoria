class Agenda:
    def __init__(self):
        self.pessoas = []



    def armazenaPessoa(self, nome, idade, altura):
        pessoa = [nome, idade, altura]
        if len(self.pessoas) <10:
            self.pessoas.append(pessoa)
        else:
            print('agenda atingiu o maximo disponivel')


    def removerPessoa(self,nomePessoa):
        self.pessoas.pop(self.buscarPessoa(nomePessoa) -1 )

    def buscarPessoa(self,nomePessoa):
        for i in range(len(self.pessoas)):
            if self.pessoas[i][0] == nomePessoa:
                return(i+1)
    
    def imprimirAgenda(self):
        for i, p in enumerate (self.pessoas):
            print(i+1,'nome:',p[0])
    
    def imprimirPessoa(self, indice):
        print('-'* 50)
        print('nome:',self.pessoas[indice][0])
        print('idade:',self.pessoas[indice][1])
        print('altura:',self.pessoas[indice][2])
        print('-'* 50)





