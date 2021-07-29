from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RoomSerializer, CreateRoomSerializer
from .models import Room

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# def welcome(request):
#     return HttpResponse("<h2>hello there</h2>")

# class RoomView(generics.CreateAPIView):
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


# view to create a room
class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer

    def post(self, request, format=None):
        # get access to session id
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        # take all data and serialize it and gie a python representation
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # create a room
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key

            # if user has a room already
            queryset = Room.objects.filter(host=host)
            
            if queryset.exists():
                room = queryset[0] # get active room
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                #update the room
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)

            # else we are creating a new room
            else:
                room = Room(host=host, guest_can_pause=guest_can_pause, votes_to_skip=votes_to_skip)
                room.save()
                return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)

            # return response to whoever created the room if this was valid or not
            # serialize the room object we just updated
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
