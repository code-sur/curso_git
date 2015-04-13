import unittest

from models import Perro, Oveja


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
        self.assertEqual("meee", oveja.balar())

    def test_deberia_ser_blanca(self):
        oveja = Oveja()
        self.assertEqual("blanca", oveja.color)


if __name__ == '__main__':
    unittest.main()
