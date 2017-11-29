from django import forms

from models import PropertiesSubmit

class AddPropForm(forms.Form):

    title = forms.CharField(label='title', max_length=50)
    address = forms.CharField(label='address', max_length=100)
    description = forms.CharField(label='description', max_length=100)
    image = forms.ImageField(required = False)


class ApproveForm(forms.Form):
	
	choices = forms.ModelMultipleChoiceField( 
		queryset = PropertiesSubmit.objects.all(), 
		widget = forms.CheckboxSelectMultiple)
	# title = forms.CharField(label='title', max_length=100)
	# address = forms.CharField(label='address', max_length=100)
	# description = forms.CharField(label='description', max_length=100)
	# image = forms.ImageField(required = False)



    



