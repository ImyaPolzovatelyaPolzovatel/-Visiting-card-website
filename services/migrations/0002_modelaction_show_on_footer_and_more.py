# Generated by Django 4.0.5 on 2022-07-06 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelaction',
            name='show_on_footer',
            field=models.BooleanField(default=False, verbose_name='Показывать на футере'),
        ),
        migrations.AddField(
            model_name='modelproduct',
            name='show_on_footer',
            field=models.BooleanField(default=False, verbose_name='Показывать на футере'),
        ),
        migrations.AddField(
            model_name='modelсategory',
            name='show_on_footer',
            field=models.BooleanField(default=False, verbose_name='Показывать на футере'),
        ),
    ]
