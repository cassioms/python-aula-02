from collections import OrderedDict
from services.boi_service import BoiService


class Menu():

    def __init__(self):
        self.boi_service = BoiService()
        self.opcoes = OrderedDict([
            ('1', ('Cadastrar boi', self.boi_service.cadastrar)),
            ('2', ('Listar bois ordenados', self.boi_service.listar)),
            ('3', ('Mostrar boi mais pesado', self.boi_service.get_mais_pesado)),
            ('4', ('Mostrar boi mais leve', self.boi_service.get_mais_leve)),
            ('0', ('Sair do programa', self.sair)),
        ])


    def __repr__(self):
        representacao = ''
        for opcao in self.opcoes.items():
            representacao += f'{opcao[0]} - {opcao[1][0]}\n'
        representacao = representacao[:-1]
        return representacao


    def executar_opcao(self, escolha):
        opcao = self.opcoes.get(escolha)
        if opcao == None:
            print('Opcao invalida.')
            return 0
        else:
            return opcao[1]()


    def sair(self):
        print('Fechando a aplicacao...')
        return 1
