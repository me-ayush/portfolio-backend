from django.db import models


# Create your models here.
class Certificates(models.Model):
    certificate_name = models.CharField(max_length=100)
    certificate_link = models.CharField(max_length=100)
    certificate_issuer = models.CharField(max_length=100)
    certificate_issue_year = models.IntegerField()
    certificate_issue_month = models.IntegerField()
    certificate_issue_date = models.IntegerField()

    # class Meta:
    #     ordering = ("certificate_issue_year", "certificate_issue_month", "certificate_issue_date")

    def __str__(self):
        return f"{self.certificate_name} {self.certificate_issue_year}/{self.certificate_issue_month}/{self.certificate_issue_date}"

    def as_dict(self):
        response = {
            "certificate_name" : self.certificate_name,
            "certificate_link" : self.certificate_link,
            "certificate_issuer" : self.certificate_issuer,
            "certificate_issue_year" : self.certificate_issue_year,
            "certificate_issue_month" : self.certificate_issue_month,
            "certificate_issue_date" : self.certificate_issue_date
        }
        return response