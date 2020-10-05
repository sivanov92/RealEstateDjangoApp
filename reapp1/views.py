from django.shortcuts import render
# Imports for the serialization
from django.core import serializers 
from reapp1.models import Agents,Estates
from django.http import JsonResponse
# Create your views here.
def agents(request):
    if request.method == "GET":
        jsonserializer = serializers.get_serializer("json")
        json_serializer = jsonserializer
        json_serializer.serialize(queryset=Agents.agents.all())
        data=json_serializer.getvalue()
        return JsonResponse(data,safe=True)
    elif request.method =="POST":
        data = request.body
        for agent in serializers.deserialize('json',data):
            agentx = Agents(agent_name=agent.agent_name,agent_adress=agent.agent_adress,agent_contact_phone=agent.agent_contact_phone)
            agentx.save()
        return JsonResponse({'result':'success'})   

def estates(request):
    if request.method == "GET":
        jsonserializer = serializers.get_serializer("json")
        json_serializer = jsonserializer
        json_serializer.serialize(Estates.estates.all())
        data=json_serializer.getvalue()
        return JsonResponse(data,safe=True)
    elif request.method =="POST":
        data = request.body
        for estate in serializers.deserialize('json',data):
            estatex = Estates(estate_title=estate.estate_title,estate_description=estate.estate_description,estate_location=estate.estate_location,estate_area=estate.estate_area,estate_construction_type=estate.estate_construction_type,estate_status=estate.estate_construction_type,estate_completion_year=estate.estate_completion_year,estate_agent=estate.estate_agent )
            estatex.save()
        return JsonResponse({'result':'success'})   
