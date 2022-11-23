from .models import Company
from rest_framework import serializers


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "status",
            "last_update",
            "application_link",
            "notes",
        ]
