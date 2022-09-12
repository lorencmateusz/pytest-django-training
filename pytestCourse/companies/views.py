from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from companies.serializers import CompanySerializer
from companies.models import Company


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")


@api_view(http_method_names=["POST"])
def send_email(request):
    send_mail(subject=, message=, from_email=, recipient_list=)
    return Response({'status': 'success', 'info': 'email sent'}, status=200)