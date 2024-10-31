from django.test import TestCase
from django.urls import reverse
from .models import Candidato

class CandidatoModelTest(TestCase):
    def setUp(self):
        # Configura um objeto candidato para ser usado nos testes
        Candidato.objects.create(
            candidato_nome="Celso Lopes Filho",
            candidato_nascimento="2004-01-29",
            candidato_cpf="08876384901",
            candidato_email="celsinholf@gmail.com"
        )

    def test_nome_candidato(self):
        candidato = Candidato.objects.get(candidato_cpf="08876384901")
        self.assertEqual(candidato.candidato_nome, "Celso Lopes Filho")

    def test_get_candidato_by_cpf(self):
        url = reverse('get_by_cpf', args=["08876384901"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Celso Lopes Filho")