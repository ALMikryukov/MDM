# Generated by Django 4.0.5 on 2022-11-01 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_user_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('history', models.TextField(blank=True, max_length=850)),
            ],
        ),
        migrations.CreateModel(
            name='Condintions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=250)),
                ('logo', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PartBrend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oem', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PartItemNoOem',
            fields=[
                ('brand', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='first.partbrend')),
                ('oem', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('quant', models.IntegerField()),
                ('quant_reserved', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CarBrends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('history', models.TextField(blank=True, max_length=850)),
                ('carModels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.carmodels')),
            ],
        ),
        migrations.CreateModel(
            name='PartItemOem',
            fields=[
                ('brand', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='first.partbrend')),
                ('oem', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('quant', models.IntegerField()),
                ('quant_reserved', models.IntegerField()),
                ('analogs', models.ManyToManyField(to='first.partitemnooem')),
                ('app', models.ManyToManyField(to='first.carmodels')),
                ('cond', models.ManyToManyField(to='first.condintions')),
            ],
        ),
        migrations.AddField(
            model_name='partitemnooem',
            name='analogs',
            field=models.ManyToManyField(to='first.partitemoem'),
        ),
        migrations.AddField(
            model_name='partitemnooem',
            name='app',
            field=models.ManyToManyField(to='first.carmodels'),
        ),
        migrations.AddField(
            model_name='partitemnooem',
            name='cond',
            field=models.ManyToManyField(to='first.condintions'),
        ),
    ]
