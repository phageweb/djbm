from django.db import models
from django.utils import timezone

# Field name Type   Field size AllowZeroLength  DefaultValue
# ID  long integer, autonumber 
# Section integer 
# Table integer  
# Round integer  
# Board  integer 
# PairNS  integer 
# PairEW integer
# Declarer integer 
# NS/EW  text   2  yes 
# Contract text   10  yes 
# Result  text   10  yes 
# LeadCard text   10  yes 
# Remarks text   255  yes 
# DateLog date/time 
# TimeLog date/time 
# Processed true/false       false 
# Processed1 true/false       false 
# Processed2 true/false       false 
# Processed3 true/false       false 
# Processed4 true/false       false 
# Erased  true/false       false 

class ReceivedData(models.Model):
    receivedData_id = models.BigIntegerField(primary_key=True)
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
        return str(self.receivedData_id+"_"+self.table+"_"+self.Board+"_"+self.PairNS+"_"+self.PairEW)