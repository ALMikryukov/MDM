# Generated by Django 4.0.5 on 2022-11-09 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0037_alter_partitem_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partitem',
            name='img',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
