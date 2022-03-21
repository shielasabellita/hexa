# Generated by Django 3.2.12 on 2022-03-21 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buying', '0001_initial'),
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemprice',
            name='base_uom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.uom'),
        ),
        migrations.AddField(
            model_name='itemprice',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buying.supplier'),
        ),
        migrations.AddField(
            model_name='supplieritem',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buying.supplier'),
        ),
        migrations.AddField(
            model_name='uomconversiondetail',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.item'),
        ),
    ]
