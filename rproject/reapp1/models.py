from django.db import models

class Estates(models.Model):
    estate_id = models.AutoField(primary_key=True)
    estate_title = models.CharField(max_length=100)
    estate_description = models.CharField(max_length=500)
    estate_location = models.CharField(max_length=200)
    estate_area = models.CharField(max_length=4)
    estate_construction_type = models.CharField(max_length=100)
    estate_status = models.CharField(max_length=20)
    estate_completion_year = models.CharField(max_length=4)

class Agents(models.Model):
    agent_id = models.AutoField(primary_key=True)
    agent_name = models.CharField(max_length=100)
    agent_adress = models.CharField(max_length=200)
    agent_contact_phone = models.CharField(max_length=100)    