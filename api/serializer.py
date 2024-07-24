from rest_framework import serializers
from members.models import *

class PlayerSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Player
        fields='__all__'
        