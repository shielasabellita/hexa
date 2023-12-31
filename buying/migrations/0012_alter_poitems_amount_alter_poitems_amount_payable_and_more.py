# Generated by Django 4.1.1 on 2022-11-02 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buying', '0011_rename_net_purchase_rate_poitems_amount_payable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poitems',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='poitems',
            name='amount_payable',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='poitems',
            name='gross_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='poitems',
            name='net_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='poitems',
            name='rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='poitems',
            name='vat_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='net_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
