from unittest.mock import *
from unittest import TestCase
from unittest import main


class AlgumaClasse:
    def _metodo_escondido(self):
        return 0

    def metodo_publico(self, x):
        return self._metodo_escondido() + x


class test_AlgumaClasse_interface_publica(TestCase):
    @patch.object(AlgumaClasse, "_metodo_escondido")
    def test_metodo_publico(self, mock_metodo):
        mock_metodo.return_value = 10
        test_objeto = AlgumaClasse()
        result = test_objeto.metodo_publico(5)
        self.assertEqual(15, result, "valor retornado de metodo_publico incorreto")
