# Generated by Django 3.1.11 on 2021-06-17 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0004_auto_20210617_1851'),
        ('trains', '0002_auto_20210617_1141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='train',
            options={'verbose_name': 'Поезд', 'verbose_name_plural': 'Поезда'},
        ),
        migrations.AlterField(
            model_name='train',
            name='city_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_from_set', to='cities.city', verbose_name='Из города'),
        ),
        migrations.AlterField(
            model_name='train',
            name='city_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_to_set', to='cities.city', verbose_name='В город'),
        ),
    ]
