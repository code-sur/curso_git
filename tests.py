import unittest

from models import Perro, Oveja, Gato


class TestPerro(unittest.TestCase):

    def test_deberia_ladrar(self):
        perro = Perro()
        self.assertEqual("ruido de perro", perro.ladrar())

    def test_deberia_ser_marron(self):
        perro = Perro()
        self.assertEqual("marron", perro.color)


class TestOveja(unittest.TestCase):

    def test_deberia_balar(self):
        oveja = Oveja()
        self.assertEqual("ruido de oveja", oveja.balar())

    def test_deberia_ser_blanca(self):
        oveja = Oveja()
        self.assertEqual("blanca", oveja.color)


class TestGato(unittest.TestCase):

    def test_deberia_maullar(self):
        gato = Gato()
        self.assertEqual("ruido de gato", gato.maullar())

    def test_deberia_ser_naranja(self):
        gato = Gato()
        self.assertEqual("naranja", gato.color)


if __name__ == '__main__':
    unittest.main()
