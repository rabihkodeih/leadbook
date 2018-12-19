from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=256)
    security_code = models.CharField(max_length=16, blank=True, null=True)
    office_address = models.TextField(blank=True, bull=True)
    email_address = models.CharField(max_length=256, blank=True, null=True)
    country = models.CharField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=256, blank=True, null=True)
    fax = models.CharField(max_length=256, blank=True, null=True)
    npwp = models.CharField(max_length=256, blank=True, null=True)
    company_website = models.CharField(max_length=256, blank=True, null=True)
    ipo_date = models.CharField(max_length=16, blank=True, null=True)
    board = models.CharField(max_length=256, blank=True, null=True)
    sector = models.CharField(max_length=256, blank=True, null=True)
    sub_sector = models.CharField(max_length=256, blank=True, null=True)
    registrar = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.company_name


class Secretary(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=256, blank=True, null=True)
    company = models.ForeignKey(Company, related_name='corporate_secretary', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=256)
    position = models.CharField(max_length=256, blank=True, null=True)
    company = models.ForeignKey(Company, related_name='director', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subsidiary(models.Model):
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=256, blank=True, null=True)
    total_asset = models.FloatField(blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    company = models.ForeignKey(Company, related_name='subsidiary', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# end of file
