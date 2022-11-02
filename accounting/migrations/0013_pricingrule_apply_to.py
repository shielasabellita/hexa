# Generated by Django 4.1.1 on 2022-10-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0012_remove_discountgroup_discounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricingrule',
            name='apply_to',
            field=models.CharField(choices=[('Item', 'Item'), ('Supplier', 'Supplier'), ('Customer', 'Customer')], max_length=20),
            preserve_default=False,
        ),
    ]