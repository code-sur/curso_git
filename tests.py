import unittest

from models import Perro, Oveja, Gato, Pajaro, Vaca


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


class TestPajaro(unittest.TestCase):

    def test_deberia_piar(self):
        pajaro = Pajaro()
        self.assertEqual("ruido de pajaro", pajaro.piar())

    def test_deberia_ser_amarillo(self):
        pajaro = Pajaro()
        self.assertEqual("amarillo", pajaro.color)


class TestVaca(unittest.TestCase):

    def test_deberia_mugir(self):
        vaca = Vaca()
        self.assertEqual("ruido de vaca", vaca.mugir())

    def test_deberia_ser_negra(self):
        vaca = Vaca()
        self.assertEqual("negra", vaca.color)


if __name__ == '__main__':
    unittest.main()
