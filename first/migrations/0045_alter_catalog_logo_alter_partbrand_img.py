# Generated by Django 4.0.5 on 2022-11-22 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0044_alter_carbrands_options_alter_carmodels_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='logo',
            field=models.ImageField(blank=True, upload_to='Category_logo'),
        ),
        migrations.AlterField(
            model_name='partbrand',
            name='img',
            field=models.ImageField(blank=True, upload_to='PartBrands'),
        ),
    ]