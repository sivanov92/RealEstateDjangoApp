from django import forms
from reapp1.models import Agents

class EstateForm(forms.Form):
    estate_title = forms.CharField(widget=forms.TextInput(attrs={'class':'EstateInputs','id':'ETtitle'}),label='Estate Tittle',max_length=80)
    estate_description = forms.CharField(label='Estate Description',max_length=300)
    estate_location = forms.CharField(label='Estate Location',max_length=100)
    estate_area = forms.IntegerField(label='Estate Area',max_value=20000)
    estate_construction_type = forms.CharField(label='Construction type',max_length=50)
    estate_status=forms.CharField(label='Status',max_length=100)
    estate_completion_year = forms.IntegerField(label="Completion Year",max_value=2050)
    estate_agent = forms.ModelChoiceField(queryset=Agents.agents.all(),empty_label="Select an Agent")

class AgentForm(forms.Form):
    agent_name = forms.CharField(label='Agent Name',max_length=100)
    agent_address = forms.CharField(label='Agent Address',max_length=300)
    agent_contact_phone = forms.CharField(label='Agent Contact Phone',max_length=12)
