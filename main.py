from interactions.menu import Menu

if __name__ == '__main__':
    menu = Menu()
    sair = 0
    while not sair:
        print(menu)
        sair = menu.executar_opcao(input('Escolha uma opcao: '))
