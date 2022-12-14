# Generated by Django 4.0.5 on 2022-11-22 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0047_remove_partitem_img_alter_partitem_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodels',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='partbrand',
            name='img',
        ),
        migrations.AlterField(
            model_name='carmodels',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='CarModels'),
        ),
        migrations.AlterField(
            model_name='conditions',
            name='logo',
            field=models.ImageField(blank=True, upload_to='Condition_logo'),
        ),
        migrations.AlterField(
            model_name='partbrand',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='PartBrands'),
        ),
    ]
