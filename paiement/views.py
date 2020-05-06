from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.contrib.auth.models import Group, User 
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.forms import ModelForm
import re
from django.db.models import Q
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
import urllib
from decimal import Decimal
from django.template import loader
from django import template
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.forms import AuthenticationForm
import urllib.request
from django.views.generic import View

from .models import *
from .utils import random_string_generator

# Create your views here.



######################################################################################
#																					 #
#                                 MANAGE PVIT SITE                                   #
#																					 #
######################################################################################

# Acceuil
def index(request):
	reference = random_string_generator()
	return render(request, 'paiement/index.html', {'reference':reference})

# Url_callback
def url_call_back_pvit(request):
	print(urllib.request.urlopen('http://pvit2.pythonanywhere.com/url_call_back_pvit/').read(1000))

# Statut_paiement
def statut_paiement(request):
	statut = request.GET['statut']
	reference = request.GET['reference']

	if reference and statut:
		paie = Transaction.objects.get(reference=reference)
		if paie and paie.statut == 200:
			paie.is_payed = True
			paie.save()
			message = 'Payement effectué avec succès !!!'
			return render(request, 'paiement/succes.html', {'message':message, 'statut':statut, 'reference':reference})
		else:
			message = 'Payement echoué !!!'
			return render(request, 'paiement/echec.html', {'message':message, 'statut':statut, 'reference':reference})
	message = 'Erreur !!!'
	return render(request, 'paiement/error.html', {'message':message, 'statut':statut, 'reference':reference})

