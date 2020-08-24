from django.shortcuts import render
# Imports for the serialization
from django.core import serializers 
from models import Agents,Estates
from django.http import JsonResponse
# Create your views here.
def agents(request):
    if request.method == "GET":
        jsonserializer = serializers.get_serializer("json")
        json_serializer = jsonserializer
        json_serializer.serialize(Agents.agents.all())
        data=json_serializer.getvalue()
        return JsonResponse(data,safe=True)
    elif request.method =="POST":
        return JsonResponse({'message':'RESPONSE'})   
