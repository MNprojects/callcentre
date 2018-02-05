# Generated by Django 2.0.1 on 2018-02-05 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('dateUploaded', models.DateField(auto_now_add=True)),
                ('accountNumber', models.IntegerField()),
                ('phoneNumber', models.CharField(max_length=20)),
                ('dialledNumber', models.IntegerField()),
                ('destination', models.CharField(max_length=20)),
                ('dateOfCall', models.DateField()),
                ('timeOfCall', models.TimeField()),
                ('usageType', models.CharField(max_length=20)),
                ('usageSubType', models.CharField(max_length=20)),
                ('transmissionType', models.CharField(max_length=20)),
                ('duration', models.DurationField()),
                ('uplinkVolume', models.IntegerField()),
                ('downlinkVolume', models.IntegerField()),
                ('totalVolume', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('bundleType', models.CharField(max_length=20)),
                ('roamedCategory', models.CharField(max_length=20)),
                ('network', models.CharField(max_length=20)),
                ('usageDirection', models.CharField(max_length=20)),
                ('billSequenceNumber', models.IntegerField()),
                ('invoiceNumber', models.IntegerField()),
            ],
        ),
    ]
