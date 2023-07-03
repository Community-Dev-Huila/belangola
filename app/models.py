from django.db import models
from app.defs import validate_bi


# Create your models here.
class Provincias(models.Model):
    def huila(self):
        pass

    def luanda(self):
        pass

    def benguela(self):
        pass

    def cabinda(self):
        pass

    def bie(self):
        pass

    def bengo(self):
        pass

    def malanje(self):
        pass

    def moxico(self):
        pass

    def kwanza_sul(self):
        pass

    def kwanza_norte(self):
        pass

    def uige(self):
        pass

    def zaire(self):
        pass

    def lunda_norte(self):
        pass

    def lunda_sul(self):
        pass

    def cunene(self):
        pass

    def namibe(self):
        pass

    def cuando_cubango(self):
        pass

    def huambo(self):
        pass


class Municipios(models.Model):
    pass


class NumeroBI(models.Model):
    numero_bi = models.CharField(max_length=14)
    is_valid = validate_bi(numero_bi)
