from rest_framework import serializers

from .models import Room


# Room serializer : Obtain json format information on Rooms
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        # fields = '__all__'
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')
