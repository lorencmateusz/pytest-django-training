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

companies_url = reverse("companies-list")
pytestmark = pytest.mark.django_db


def test_zero_companies_return_empty_list(client) -> None:
    response = client.get(companies_url)
    assert response.status_code == 200
    print(response.status_code)


def test_one_company_return_should_succeed(client) -> None:
    amazon = Company.objects.create(name='Amazon')
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]['name']
    assert response_content == 'Amazon'


def test_create_company_without_arguments_should_fail(client):
    response = client.post(path=companies_url)
    response_status = response.status_code
    response_content = json.loads(response.content)['name']
    assert response_content == ['This field is required.']
    assert response_status == 400


def test_add_existing_company_should_fail(client) -> None:
    Company.objects.create(name='Apple')
    response = client.post(path=companies_url, data={'name' : 'Apple'})
    response_status = response.status_code
    response_content = json.loads(response.content)['name']
    assert response_content == ['company with this name already exists.']
    assert response_status == 400


def test_add_company_with_only_name_should_return_defaults(client) -> None:
    response = client.post(path=companies_url, data={'name': 'test company'})
    response_status = response.status_code
    response_content = json.loads(response.content)
    assert response_content['name'] == 'test company'
    assert response_content['status'] == 'Hiring'
    assert response_content['notes'] == ''
    assert response_status == 201


