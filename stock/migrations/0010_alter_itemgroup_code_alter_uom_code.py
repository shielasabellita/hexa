# Generated by Django 4.0.5 on 2022-09-04 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_alter_item_code_alter_supplieritem_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemgroup',
            name='code',
            field=models.CharField(default='ITM-GRP_{5}', max_length=120),
        ),
        migrations.AlterField(
            model_name='uom',
            name='code',
            field=models.CharField(default='UOM_{5}', max_length=120),
        ),
    ]
