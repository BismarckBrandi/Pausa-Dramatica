from models.models import Model

class Passeio(Model):
    def oferecerPasseio(self):
        v=0
        ponto = self.get(ponto = self.ponto)
        for i in range(len(ponto)):
            if ponto[i][3] == self.data:
                v=1
        if v==0:
            self.save()
            return True
        else:
            return False