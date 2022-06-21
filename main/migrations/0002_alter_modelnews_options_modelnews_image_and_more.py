# Generated by Django 4.0.5 on 2022-06-21 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modelnews',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='modelnews',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='modelnews',
            name='descriptionShort',
            field=models.CharField(max_length=20, verbose_name='Краткое описание'),
        ),
    ]