# Generated by Django 4.0.5 on 2022-11-07 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0029_alter_partitem_quantaty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partitem',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='first.partbrand'),
        ),
    ]
