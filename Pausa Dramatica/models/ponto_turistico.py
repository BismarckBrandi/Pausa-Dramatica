from models.models import Model

class PontoTuristico(Model):
    def criarPonto(self):
        ponto = self.get(name = self.name)

        if len(ponto) == 0:
            self.save()
            return True
        else:
            return False
