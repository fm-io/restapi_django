from django.shortcuts import render
from rest_framework import viewsets
from .models import Waitlist
from .serializers import WaitlistSerializer




# Create your views here. //create API view
class WaitlistViewSet(viewsets.ModelViewSet):
    queryset = Waitlist.objects.all()
    serializer_class = WaitlistSerializer
