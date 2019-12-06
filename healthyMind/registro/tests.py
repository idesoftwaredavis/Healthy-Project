from django.test import TestCase
from .models import Registro

class RegistroTestCase(TestCase):
    def setUp(self):
        self.usuario1 = Registro(nombre="testcase1", email = "testcase1@gmail.com", contrasenia = "chelsea")
        self.usuario2 = Registro(nombre="testcase2", email = "testcase2@gmail.com",contrasenia = "chelsea1")

    def test_mostrar_alumno(self):
        usuario = Registro.objects.filter(nombre= self.usuario1).get()
        self.assertEqual(usuario ,"testcase1")
