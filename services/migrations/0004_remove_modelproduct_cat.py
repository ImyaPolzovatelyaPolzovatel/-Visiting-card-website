# Generated by Django 4.0.5 on 2022-07-08 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_modelсategory_prod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelproduct',
            name='cat',
        ),
    ]