# Generated by Django 4.0.5 on 2022-11-08 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0035_alter_carmodels_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodels',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='partitem',
            name='app',
            field=models.ManyToManyField(blank=True, to='first.carmodels'),
        ),
    ]