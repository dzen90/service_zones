# Generated by Django 3.1.4 on 2020-12-05 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zones', '0003_servicetype'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServiceType',
            new_name='Service',
        ),
        migrations.AddField(
            model_name='zone',
            name='services',
            field=models.ManyToManyField(to='zones.Service'),
        ),
    ]
