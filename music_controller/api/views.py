from django.shortcuts import render

from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.

# def welcome(request):
#     return HttpResponse("<h2>hello there</h2>")

# class RoomView(generics.CreateAPIView):
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
