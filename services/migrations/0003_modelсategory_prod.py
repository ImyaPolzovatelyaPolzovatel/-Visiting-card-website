# Generated by Django 4.0.5 on 2022-07-07 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_modelaction_show_on_footer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelсategory',
            name='prod',
            field=models.ManyToManyField(to='services.modelproduct', verbose_name='Услуги'),
        ),
    ]
