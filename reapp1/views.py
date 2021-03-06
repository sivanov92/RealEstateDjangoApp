from django.shortcuts import render
# Imports for the serialization
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from reapp1.models import Agents,Estates
from django.http import JsonResponse,HttpResponseRedirect
from .forms import EstateForm,AgentForm
# Create your views here.
def addEstate(request):
    if request.method == 'POST':
        form = EstateForm(request.POST)
        if form.is_valid():
            estate_obj = Estates(estate_title=form.cleaned_data['estate_title'],
                                 estate_description=form.cleaned_data['estate_description'],
                                 estate_location=form.cleaned_data['estate_location'],
                                 estate_area=form.cleaned_data['estate_area'],
                                 estate_construction_type=form.cleaned_data['estate_construction_type'],
                                 estate_status=form.cleaned_data['estate_status'],
                                 estate_completion_year=form.cleaned_data['estate_completion_year'],
                                 estate_agent=form.cleaned_data['estate_agent'])
            estate_obj.save()                            
    else:
        form = EstateForm()  
        #choices = []
        #for agent in Agents.agents.all():
        #    info = (agent.agent_name,agent.agent_name)
        #    choices.append(info)
        #form.fields['estate_agent'].choices = choices          
    return render(request,'addEstate.html',{'form':form})
#--
def addAgent(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            agent_obj = Agents(agent_name=form.cleaned_data['agent_name'],
                                agent_adress=form.cleaned_data['agent_address'],
                                agent_contact_phone=form.cleaned_data['agent_contact_phone'])
            agent_obj.save()                            
    else:
        form = AgentForm()        
    return render(request,'addAgent.html',{'form':form})
#--------
def seeEstates(request):
    element_list =list(Estates.estates.all())
    context = {
        'element_list':element_list,
        'exists':Estates.estates.exists()
    }
    return render(request,'miniestatepreview.html',context)
#---------    
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
