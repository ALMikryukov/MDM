# Generated by Django 4.0.5 on 2022-11-01 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0010_alter_partitemnooem_quant_reserved_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partitemnooem',
            name='quant_reserved',
        ),
        migrations.RemoveField(
            model_name='partitemoem',
            name='quant_reserved',
        ),
    ]