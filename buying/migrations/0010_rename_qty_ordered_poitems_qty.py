# Generated by Django 4.1.1 on 2022-11-01 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buying', '0009_poitems_net_purchase_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poitems',
            old_name='qty_ordered',
            new_name='qty',
        ),
    ]