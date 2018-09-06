import sqlite3

from models.boi import Boi


class BoiService:

    def __init__(self):
        with sqlite3.connect('bois.db') as conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS boi (id NUMBER, nome TEXT, peso NUMBER)')
            cursor.close()
        conn.close()


    def connected(self, funcao, *args):
        with sqlite3.connect('bois.db') as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            retorno_funcao = funcao(conn, cursor, *args)
            cursor.close()
        conn.close()
        return retorno_funcao


    def cadastrar(self):
        def cadastrar_boi(conn, cursor, bid, nome, peso):
            cursor.execute('INSERT INTO boi VALUES (?, ?, ?)', (bid, nome, peso))
            conn.commit()

        try:
            boi_id = int(input('Entre com o id: '))
            nome = input('Entre com o nome: ')
            peso = float(input('Entre com o peso: '))
            self.connected(cadastrar_boi, boi_id, nome, peso)
        except:
            print('Erro ao inserir boi')

        return 0


    def listar(self):
        def listar_bois(conn, cursor):
            bois = self.get_bois(cursor)
            print(bois)
        self.connected(listar_bois)
        return 0


    def get_mais_pesado(self):
        def get_mais_pesado(conn, cursor):
            bois = self.get_bois(cursor)
            print(bois[0])

        self.connected(get_mais_pesado)
        return 0


    def get_mais_leve(self):
        def get_mais_leve(conn, cursor):
            bois = self.get_bois(cursor)
            print(bois[-1:])
        self.connected(get_mais_leve)
        return 0


    def get_bois(self, cursor):
        cursor.execute('SELECT * FROM boi')
        bois = list(map(lambda boi: Boi(boi), cursor.fetchall()))
        bois.sort()
        return bois
