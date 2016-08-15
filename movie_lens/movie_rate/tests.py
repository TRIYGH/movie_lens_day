from django.test import TestCase

from movie_rate.models import Rater


class RaterTestCase(TestCase):
    def setUp(self):
        Rater.objects.create(age=44, gender='M', occupation='tech', zipcode='28473')
        Rater.objects.create(age=22, gender='F', occupation='teacher', zipcode='32467')

    def test_Rater(self):
        man = Rater.objects.get(age=44)
        woman = Rater.objects.get(age=22)
        self.assertEqual(man.gender='M')
        self.assertEqual(woman.gender='F')
