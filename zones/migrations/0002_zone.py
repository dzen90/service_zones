# Generated by Django 3.1.4 on 2020-12-05 21:20

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('zone', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zones.supplier')),
            ],
        ),
    ]
