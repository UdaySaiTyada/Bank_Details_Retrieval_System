from django.db import models

class Banks(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ifsc = models.CharField(max_length=30, blank=True, null=True)
    bank_id = models.BigIntegerField(blank=True, null=True)
    branch = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    district = models.CharField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)
    bank_name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banks'