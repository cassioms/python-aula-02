class Boi:

    def __init__(self, boi):
        self.id = boi['id']
        self.nome = boi['nome']
        self.peso = boi['peso']


    def __gt__(self, outro):
        if self.peso == outro.peso:
            return self.id > outro.id
        return self.peso < outro.peso


    def __repr__(self):
        return f'<Id:{self.id}|Nome:{self.nome}|Peso:{self.peso}>'
