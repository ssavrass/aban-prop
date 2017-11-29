from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

from properties.models import Properties, PropertiesSubmit
from django.template import RequestContext
from django.shortcuts import render_to_response
# from django.core.paginator import Paginator
from django.http import HttpRequest

from social_django.models import UserSocialAuth
import datetime

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from properties.serializers import PropertiesSerializer
# from rest_framework import permissions

from forms import AddPropForm, ApproveForm

import re
import json
import urllib



class PropertiesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Properties.objects.all()
    serializer_class = PropertiesSerializer
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(request, user)
            return redirect('properties')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def properties(request):
	
	if request.method == 'POST':

		form = AddPropForm(request.POST, request.FILES)

		if form.is_valid():    
			# print form.cleaned_data
			title = form.cleaned_data['title']
			address = form.cleaned_data['address']
			description = form.cleaned_data['description']
			image = form.cleaned_data['image']



			PropertiesSubmit.create('', '', title,address,description,image).save()


			return redirect('properties')
		else:
			print "invalid form"	

	return render(request, 'properties.html')




def aboutus(request):
    return render(request, 'aboutus.html')


def propdetails(request, id):
	result = Properties.objects.get(id = id)
	form = AddPropForm(request.POST, request.FILES)

	if form.is_valid():    
		# print form.cleaned_data
		title = form.cleaned_data['title']
		address = form.cleaned_data['address']
		description = form.cleaned_data['description']
		image = form.cleaned_data['image']



		result.title = title
		result.address = address
		result.description = description
		result.image = image


		return redirect('propdetails')

	return render(request, 'propdetails.html', {'result': result}) 

@login_required
def propsubdetails(request, id):
	result = PropertiesSubmit.objects.get(id = id)
	form = AddPropForm(request.POST, request.FILES)
	#print form
	if form.is_valid():    
		
		title = form.cleaned_data['title']
		address = form.cleaned_data['address']
		description = form.cleaned_data['description']
		image = form.cleaned_data['image']

		result.title = title
		result.address = address
		result.description = description
		if image != None:
			result.image = image

		result.save()


		return redirect('approveproperties')
	else:
		print "Invalid form"	
    
	return render(request, 'propsubdetails.html', {'result': result})     

@login_required
def approveproperties(request):
	results = PropertiesSubmit.objects.all()
	if request.method == 'POST':
		if 'approve' in request.POST:
			form = ApproveForm(request.POST)

			if form.is_valid(): 


				choices = form.cleaned_data['choices']

				for choice in choices:
					url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + choice.address.encode('utf-8') + '&key=AIzaSyBiB5iKNfCbMFqX70ULP039rt1QZV1zs0s'
					response = urllib.urlopen(url)
					location_data = json.loads(response.read())


					location = location_data['results'][0]['geometry']['location']

					lat = location['lat']
					lon = location['lng']
					prop = Properties.create(lon, lat, choice.title, choice.address, choice.description, choice.image).save()
					print prop
					PropertiesSubmit.objects.get(id=choice.id).delete()	


		return redirect('approveproperties')	

		if 'delete' in request.POST:
			form = ApproveForm(request.POST)
			if form.is_valid(): 
				#print form.cleaned_data['choices']

				choices = form.cleaned_data['choices']	

				for choice in choices:
					print choice.id
					PropertiesSubmit.objects.get(id=choice.id).delete()	

				return redirect('approveproperties')
			
	else:
	
		form = ApproveForm






	return render(request, 'approveproperties.html' , {'results': results, 'form': form})

@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None
    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None
    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'password.html', {'form': form})
