# Generated by Django 4.0.5 on 2022-11-03 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0022_alter_partitem_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partitem',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='first.catalog'),
        ),
    ]
