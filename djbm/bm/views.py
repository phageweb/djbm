from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from bm.serializers import UserSerializer, GroupSerializer, ReceivedDataSerializer,SectionSerializer, TablesSerializer, ClientsSerializer
from bm.models import ReceivedData, Section, Tables, Clients


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ReceivedDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ReceivedData.objects.all()
    serializer_class = ReceivedDataSerializer

class SectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class TablesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tables.objects.all()
    serializer_class = TablesSerializer    

class ClientsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer    