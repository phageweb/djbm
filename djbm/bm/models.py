from django.db import models
from django.utils import timezone

class Clients(models.Model):
    clients_id = models.AutoField(primary_key=True)
    Computer   = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.clients_id)

class Section(models.Model):
    Section = models.IntegerField() 
    Table = models.IntegerField() 
    ComputerID = models.IntegerField(default='0') 
    Status = models.IntegerField(default='0') 
    LogOnOff = models.IntegerField(default='2') 
    UpdateFromRoad = models.IntegerField(default='0') 
    CurrentRound = models.IntegerField(default='0') 
    CurrentBoard = models.IntegerField(default='0') 
    Group = models.IntegerField(default='0') 
    
    def __str__(self):
        return str(self.receivedData_id)


class Tables(models.Model):
    Section = models.IntegerField() 
    Table = models.IntegerField() 
    Round = models.IntegerField() 
    PairNS = models.IntegerField() 
    PairEW = models.IntegerField() 
    LowBoard = models.IntegerField() 
    HighBoard = models.IntegerField() 
    CustomBoard = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.receivedData_id)
class ReceivedData(models.Model):
    receivedData_id = models.BigIntegerField()
    Section = models.IntegerField() 
    Table = models.IntegerField() 
    Round = models.IntegerField() 
    Board = models.IntegerField() 
    PairNS = models.IntegerField() 
    PairEW = models.IntegerField() 
    Declarer = models.IntegerField() 
    NS_EW       = models.CharField(max_length=2)
    Contract    = models.CharField(max_length=10)
    Result    = models.CharField(max_length=10)
    LeadCard    = models.CharField(max_length=10)
    Remarks    = models.CharField(max_length=255)
    Processed = models.BooleanField(default=False)
    Processed1 = models.BooleanField(default=False)
    Processed2 = models.BooleanField(default=False)
    Processed3 = models.BooleanField(default=False)
    Processed4 = models.BooleanField(default=False)
    Erased = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return str(self.receivedData_id)