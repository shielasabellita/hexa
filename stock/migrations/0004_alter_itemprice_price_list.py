# Generated by Django 3.2.12 on 2022-03-28 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_discountgroup'),
        ('stock', '0003_alter_item_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemprice',
            name='price_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.pricelist'),
        ),
    ]
