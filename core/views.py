# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.core.mail import send_mail

def send(request):
	# email = "from@example.com"
	email = request.GET.get('email')
	if email and '@' in email:
		body = 'This is a test message sent to {}.'.format(email)
		send_mail('Hello', body, 'noreply@mysite.com', [email, ])
		return HttpResponse('<h1>Sent.</h1>')
	else:
		return HttpResponse('<h1>No email was sent.</h1>')