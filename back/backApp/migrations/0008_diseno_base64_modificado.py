# Generated by Django 2.2.4 on 2019-09-05 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backApp', '0007_auto_20190905_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseno',
            name='base64_modificado',
            field=models.CharField(max_length=500000, null=True),
        ),
    ]
