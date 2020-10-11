from django.db import models

class Agents(models.Model):
    agent_name = models.CharField(max_length=100,primary_key=True)
    agent_adress = models.CharField(max_length=200)
    agent_contact_phone = models.CharField(max_length=100)    
    agents = models.Manager()
    def __str__(self):
        return self.agent_name

class Estates(models.Model):
    estate_id = models.AutoField(primary_key=True)
    estate_title = models.CharField(max_length=100)
    estate_description = models.CharField(max_length=500)
    estate_location = models.CharField(max_length=200)
    estate_area = models.CharField(max_length=4)
    estate_construction_type = models.CharField(max_length=100)
    estate_status = models.CharField(max_length=20)
    estate_completion_year = models.CharField(max_length=4)
    estate_agent = models.ForeignKey(Agents,on_delete=models.CASCADE)
    estates=models.Manager()
    