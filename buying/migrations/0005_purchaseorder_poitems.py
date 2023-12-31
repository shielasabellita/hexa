# Generated by Django 4.0.5 on 2022-07-17 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0006_remove_discountgroup_discount1_and_more'),
        ('stock', '0006_itemcatbrand_itemcatdepartment_itemcategory_and_more'),
        ('setup', '0002_statusandrcode'),
        ('buying', '0004_auto_20220322_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=120)),
                ('date', models.DateField(auto_now_add=True)),
                ('date_expected', models.DateField(auto_now_add=True)),
                ('total_amount', models.DecimalField(decimal_places=4, default=0, max_digits=10)),
                ('net_amount', models.DecimalField(decimal_places=4, default=0, max_digits=10)),
                ('apply_tax', models.CharField(choices=[(1, 1), (0, 0)], default=0, max_length=1)),
                ('created_by', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.branch')),
                ('cost_center', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.costcenter')),
                ('fixed_asset_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.fixedassetgroup')),
                ('item_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.itemgroup')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.location')),
                ('price_list', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.pricelist')),
                ('reason_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.statusandrcode')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buying.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='POItems',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=120)),
                ('item_description', models.CharField(blank=True, max_length=120)),
                ('item_shortname', models.CharField(blank=True, max_length=120)),
                ('qty_ordered', models.FloatField(default=0, max_length=10)),
                ('rate', models.DecimalField(decimal_places=4, default=0, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=4, default=0, max_digits=10)),
                ('created_by', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.item')),
                ('price_rule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.pricingrule')),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buying.purchaseorder')),
                ('uom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.uom')),
                ('vat_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.vatgroup')),
            ],
        ),
    ]
