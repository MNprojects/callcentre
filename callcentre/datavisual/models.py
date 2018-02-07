from django.db import models

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class CallRecord(models.Model):
    
    
    accountNumber = models.IntegerField()
    phoneNumber = models.CharField(max_length=20)
    dialledNumber = models.IntegerField()
    destination = models.CharField(max_length=20)
    dateOfCall = models.DateField()
    timeOfCall = models.TimeField()
    usageType = models.CharField(max_length=20)
    usageSubType = models.CharField(max_length=20)
    transmissionType = models.CharField(max_length=20)
    duration = models.DurationField()
    uplinkVolume = models.IntegerField()
    downlinkVolume = models.IntegerField()
    totalVolume = models.IntegerField()
    cost = models.DecimalField(decimal_places=2, max_digits=7)
    bundleType = models.CharField(max_length=20)
    roamedCategory = models.CharField(max_length=20)
    network = models.CharField(max_length=20)
    usageDirection = models.CharField(max_length=20)
    billSequenceNumber = models.IntegerField()
    invoiceNumber = models.IntegerField()
    