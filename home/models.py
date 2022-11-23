from django.db import models

# Create your models here.
class Company(models.Model):
    class CompanyStatus(models.TextChoices):
        LAYOFFs = "Layoffs"
        HIRING_FREEZE = "HIRING FREEZE"
        HIRING = "Hiring"

    name = models.CharField(max_length=50, unique=True)
    status = models.CharField(
        choices=CompanyStatus.choices, default=CompanyStatus.HIRING, max_length=50
    )
    last_update = models.DateTimeField(auto_now=True, editable=True)
    application_link = models.URLField(blank=True)
    notes = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return self.name
