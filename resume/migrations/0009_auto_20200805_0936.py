# Generated by Django 3.0.6 on 2020-08-05 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_auto_20200804_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='middlename',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
