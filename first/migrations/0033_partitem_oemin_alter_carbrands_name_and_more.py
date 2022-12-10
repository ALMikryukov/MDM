# Generated by Django 4.0.5 on 2022-11-08 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0032_alter_partitem_oem'),
    ]

    operations = [
        migrations.AddField(
            model_name='partitem',
            name='oemIn',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='carbrands',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='carmodels',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='partbrand',
            name='name',
            field=models.CharField(max_length=250, null=True, unique=True),
        ),
    ]