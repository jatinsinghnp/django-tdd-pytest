from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CompanySerializers
from .models import Company
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializers
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination
