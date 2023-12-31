# Generated by Django 4.0.5 on 2022-08-22 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_alter_itemprice_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.CharField(default='ITM_{9}', max_length=120),
        ),
        migrations.AlterField(
            model_name='supplieritem',
            name='code',
            field=models.CharField(default='ITM-SUP_{9}', max_length=120),
        ),
        migrations.AlterField(
            model_name='uomconversiondetail',
            name='code',
            field=models.CharField(default='UOM-CONV_{9}', max_length=120),
        ),
    ]
