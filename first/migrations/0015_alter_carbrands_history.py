# Generated by Django 4.0.5 on 2022-11-01 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0014_carbrands_rename_partbrend_partbrand_carmodels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbrands',
            name='history',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
