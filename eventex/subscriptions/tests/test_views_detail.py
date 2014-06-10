# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(name='Henrique Bastos',
                                        cpf='12345678901',
                                        email='henrique@bastos.net',
                                        phone='21-96186180')
        self.resp = self.client.get('/inscricao/%d' % s.pk)

    def test_get(self):
        'GET /inscricao/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_tempate(self):
        'Uses template'
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_detail.html')


    def test_context(self):
        'Context must have a subscription instance.'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        'Check if subscription data was rendered'
        self.assertContains(self.resp, 'Henrique Bastos')

class DetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get('/inscricao/0/')
        self.assertEqual(404, response.status_code)
