class Boi:

    def __init__(self, boi):
        self.id = boi[0]
        self.nome = boi[1]
        self.peso = boi[2]


    def __gt__(self, outro):
        if self.peso == outro.peso:
            return self.id > outro.id
        return self.peso < outro.peso


    def __repr__(self):
        return f'<Id:{self.id}|Nome:{self.nome}|Peso:{self.peso}>'
