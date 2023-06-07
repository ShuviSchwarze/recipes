from django.shortcuts import render
from django.http import JsonResponse
from . import models
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views import View

import json
from functools import wraps


class RegistrationForm(View):

    def post(self, request) -> JsonResponse:
        #username = request.POST.get("username")
        #email = request.POST.get("email")
        #password = request.POST.get("password")
        #
        #if validate_user(username, email, password) :       
        #    new_user = models.User.create(
        #        username=username,
        #        email=email,
        #        password=password,
        #    )
        #
        #json = presenter.createJSon(new_user)
        
        
        return #JsonResponse()