from django.shortcuts import render
# Imports for the serialization
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from reapp1.models import Agents,Estates
from django.http import JsonResponse,HttpResponseRedirect
from .forms import EstateForm
# Create your views here.
def addEstate(request):
    if request.method == 'POST':
        form = EstateForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/Thanks/')
    else:
        form = EstateForm()        
    return render(request,'addEstate.html',{'form':form})

def agents(request):
    if request.method == "GET":
        jsonserializer = serializers.serialize('json',Agents.agents.all())
        return JsonResponse(jsonserializer,safe=False)
    elif request.method =="POST":
        data = request.body
        for agent in serializers.deserialize('json',data):
            #agentx = Agents(agent_name=agent.agent_name,agent_adress=agent.agent_adress,agent_contact_phone=agent.agent_contact_phone)
            agent.save()
        return JsonResponse({'result':'success'})   

def estates(request):
    if request.method == "GET":
        jsonserializer = serializers.serialize('json',Estates.estates.all())
        return JsonResponse(jsonserializer,safe=False)
    elif request.method =="POST":
        data = request.body
        for estate in serializers.deserialize('json',data):
            #estatex = Estates(estate_title=estate.estate_title,estate_description=estate.estate_description,estate_location=estate.estate_location,estate_area=estate.estate_area,estate_construction_type=estate.estate_construction_type,estate_status=estate.estate_construction_type,estate_completion_year=estate.estate_completion_year,estate_agent=estate.estate_agent )
            estate.save()
        return JsonResponse({'result':'success'})   
