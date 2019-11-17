from models.models import Model

class Usuario(Model):
    def registrar(self):
        user = self.get(username = self.username)

        if len(user) == 0:
            self.save()
            return True
        else:
            return False

    def autenticar(self):
        user = self.get(username=self.username)
        if user[0][3]== self.senha:
            return True
        else:
            return False