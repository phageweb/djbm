from django.contrib.auth.models import User, Group
from rest_framework import serializers
from bm.models import ReceivedData, Section, Tables, Clients

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ReceivedDataSerializer(serializers.HyperlinkedModelSerializer):
    #user_id = serializers.Field(source='bm.ReceivedData_id')
    class Meta:
        model = ReceivedData
        fields = '__all__'

class TablesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tables
        fields = '__all__'

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class ClientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'

