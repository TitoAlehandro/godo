#!/usr/bin/:q:python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext
from django.http import HttpResponse,  HttpResponseRedirect
def about(request):
	template = loader.get_template("about.html")
	context = RequestContext(request, {
			"tpanel_partn": "index",
			})
	return HttpResponse(template.render(context))

