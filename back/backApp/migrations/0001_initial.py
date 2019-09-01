# Generated by Django 2.2 on 2019-08-31 23:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('descripcion', models.CharField(max_length=500)),
                ('pago', models.IntegerField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backApp.Empresa')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Diseño',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('estado', models.BooleanField()),
                ('fecha', models.DateTimeField()),
                ('pago', models.IntegerField()),
                ('urlArchivo', models.CharField(max_length=500)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backApp.Proyecto')),
            ],
        ),
    ]
