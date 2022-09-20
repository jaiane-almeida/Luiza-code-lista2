
#exercicio 1
class Pessoa:
    informacoes = "documento de identidade"


    def __init__(self, nome, cpf, idade, status):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.status = status

    def descricao(self):
      if self.status == 'F':
        print('é fumante')
      elif self.status == "N":
        print('NÃO É fumante')
      else:
        print('coloque N ou F')

alguem = Pessoa('jai', 00000, 20, "N")
alguem.descricao()

#exercicio 2
class PessoaFisica(Pessoa):
    def __init__(self):
        super().__init__()

#exercicio 3
class PessoaJuridica(Pessoa):
    def __init__(self, nome, cpf, idade, status, cnpj):
        super().__init__(nome, cpf, idade, status)
        self.cnpj = cnpj


#exercicio 4

class Professor:

    # def teacher(self, nome, idade, cpf):
    #     self.nome = nome
    #     self.idade = idade
    #     self.__cpf = cpf


    def doc(self, usuario, nome, idade, cpf):
        if usuario == 'Usuario aceito':
            print(self.__apresentar_doc(nome, idade, cpf))
       # print('Pode acessar')
        elif usuario == 'Usuario recusado':
            print(self.__nao_apresentar(nome, idade, cpf))
        else:
            print('Operação invalida, tente novamente')

    def __apresentar_doc(self, nome, idade, cpf):
        return(cpf)

    def __nao_apresentar(self, nome, idade, cpf):
        return(self.__cpf)

teacher = Professor()
resultado = teacher.doc('Usuario aceito','Joao', 32, 5821)
print(resultado)

#exercicio 5
class Quadrado:
    def __init__(self, larg, comp):
        self.larg = larg
        self.comp = comp


    def area(self):
        a = self.larg*self.comp
        print(f'a area de um quadrado é {a}m²')

    def perimetro(self):
        p = (2*self.larg)+(2*self.comp)
        print(f'o perimetro de um quadrado é {p}')