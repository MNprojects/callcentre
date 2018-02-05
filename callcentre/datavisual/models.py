from django.db import models

# Create your models here.
class Record(models.Model):
    title = models.CharField(max_length=20)
    dateUploaded = models.DateField(auto_now_add=True ,null=False)
    accountNumber = models.IntegerField()
    phoneNumber = models.CharField()
    dialledNumber = models.IntegerField()
    destination = models.CharField()
    dateOfCall = models.DateField()
    timeOfCall = models.TimeField()
    usageType = models.CharField()
    usageSubType = models.CharField()
    transmissionType = models.CharField()
    duration = models.DurationField()
    uplinkVolume = models.IntegerField()
    downlinkVolume = models.IntegerField()
    totalVolume = models.IntegerField()
    cost = models.DecimalField()
    bundleType = models.CharField()
    roamedCategory = models.CharField()
    network = models.CharField()
    usageDirection = models.CharField()
    billSequenceNumber = models.IntegerField()
    invoiceNumber = models.IntegerField()
    