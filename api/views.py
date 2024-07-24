from django.shortcuts import render
from members.models import *
from rest_framework import generics
from .serializer import PlayerSerilizer

# Create your views here.
class PlayerListCreate(generics.ListCreateAPIView):
    queryset=Player.objects.all()
    serializer_class= PlayerSerilizer

class PlayerRetrieveUpdateDestory(generics.RetrieveDestroyAPIView):
    queryset=Player.objects.all()
    serializer_class=PlayerSerilizer