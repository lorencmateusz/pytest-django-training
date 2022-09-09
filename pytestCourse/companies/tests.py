import json
from unittest import TestCase

import pytest
from django.urls import reverse
from django.test import Client

from pytestCourse.wsgi import *
from companies.models import Company

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pytestCourse.settings')
django.setup()


@pytest.mark.django_db
class TestGetCompanies(TestCase):
    def test_zero_companies_return_empty_list(self) -> None:
        client = Client()
        companies_url = reverse("companies-list")
        response = client.get(companies_url)
        self.assertEqual(response.status_code, 200)

    def test_one_company_return_should_succeed(self) -> None:
        client = Client()
        amazon = Company.objects.create(name='Amazon')
        companies_url = reverse('companies-list')
        response = client.get(companies_url)
        response_content = json.loads(response.content)[0]
