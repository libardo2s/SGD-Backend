# Generated by Django 2.0.4 on 2018-04-11 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180410_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propietario',
            name='departamento',
        ),
        migrations.RemoveField(
            model_name='propietario',
            name='municipio',
        ),
        migrations.AddField(
            model_name='persona',
            name='departamento',
            field=models.CharField(max_length=30, null=True, verbose_name='Departamento'),
        ),
        migrations.AddField(
            model_name='persona',
            name='municipio',
            field=models.CharField(max_length=30, null=True, verbose_name='Municipio'),
        ),
    ]
