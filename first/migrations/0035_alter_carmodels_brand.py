# Generated by Django 4.0.5 on 2022-11-08 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0034_alter_carbrands_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodels',
            name='brand',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='first.carbrands'),
        ),
    ]
