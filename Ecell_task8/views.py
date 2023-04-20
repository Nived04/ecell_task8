from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
from django.shortcuts import redirect


class ProtectedView(TemplateView):

    template_name = "protected.html"
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        return super(ProtectedView, self).dispatch(request, *args, **kwargs)

class BioView(TemplateView):

    template_name = "biodata.html"
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        return super(BioView, self).dispatch(request, *args, **kwargs)

class EduView(TemplateView):

    template_name = "biodata/edu_bio.html"
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        return super(EduView, self).dispatch(request, *args, **kwargs)

class PlaceView(TemplateView):

    template_name = "biodata/places_bio.html"
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        return super(PlaceView, self).dispatch(request, *args, **kwargs)

class ExtraView(TemplateView):

    template_name = "biodata/extra_bio.html"
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        return super(ExtraView, self).dispatch(request, *args, **kwargs)




# Create your views here.
