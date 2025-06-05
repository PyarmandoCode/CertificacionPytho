class Corredor:
    def correr(self):
        return "Corriendo"

class Nadador:
    def nadar(self):
        return "Nadando"

class TriAtleta(Corredor,Nadador):
    pass

juan=TriAtleta()
#print(juan.correr())
#print(juan.nadar())


