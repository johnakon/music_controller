from django.db import models

import string
import random

# code for the room should be random and unique
def generate_unique_code():
    length = 6

    while True:
        # generate random code that is k length
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        # make sure this code is unique
        # check all rooms ans see if that code exists
        if Room.objects.filter(code = code).count() == 0:
            break
    
    return code

# Create your models here.

# room
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)


    def 
