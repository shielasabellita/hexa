# Generated by Django 4.0.5 on 2022-08-05 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_itemprice_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemprice',
            name='code',
            field=models.CharField(default='ITM-PRC_{9}', max_length=120),
        ),
    ]
