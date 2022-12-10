# Generated by Django 4.0.5 on 2022-11-09 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0038_alter_partitem_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodels',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='partbrand',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='partitem',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='partitem',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
