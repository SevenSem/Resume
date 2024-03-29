# Generated by Django 3.0.6 on 2020-12-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personality', '0004_personalityresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalitydata',
            name='type_a',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='personalitydata',
            name='type_c',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='personalitydata',
            name='type_e',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='personalitydata',
            name='type_n',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='personalitydata',
            name='type_o',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
