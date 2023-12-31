# Generated by Django 4.1.1 on 2023-01-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buying', '0013_rename_item_poitems_item_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poitems',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='poitems',
            old_name='uom_id',
            new_name='uom',
        ),
        migrations.AddField(
            model_name='poitems',
            name='uom_name',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
