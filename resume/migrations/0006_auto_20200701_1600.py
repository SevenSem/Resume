# Generated by Django 3.0.6 on 2020-07-01 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20200701_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalinfo',
            old_name='personalinfo',
            new_name='firstname',
        ),
    ]