from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from companies.serializers import CompanySerializer
from companies.models import Company


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
