# Generated by Django 4.0.5 on 2022-11-17 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0040_alter_carbrands_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contryes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='partbrand',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='first.contryes'),
        ),
    ]
