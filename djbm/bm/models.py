from django.db import models
from django.utils import timezone

# Field name Type   Field size AllowZeroLength  Default
# Value ID  long integer, 
# autonumber Section  
# integer Table  
# integer Round  
# integer Board  
# integer PairNS  
# integer 
# PairEW  
# integer     
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
    NS_EW = models.CharField(max_length=2)
    created_date = models.DateTimeField(
            default=timezone.now)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.receivedData_id)