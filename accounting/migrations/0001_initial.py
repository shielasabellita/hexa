# Generated by Django 3.2.12 on 2022-03-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChartOfAccounts',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=120)),
                ('account_code', models.CharField(blank=True, max_length=120)),
                ('account_name', models.CharField(max_length=120)),
                ('account_type_and_financial_group', models.CharField(blank=True, max_length=80)),
                ('normal_balance', models.CharField(blank=True, max_length=120)),
                ('report', models.CharField(blank=True, max_length=120)),
                ('is_default_expense', models.IntegerField(choices=[(1, 1), (0, 0)], default=0)),
                ('created_by', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CostCenter',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=120)),
                ('cost_center_name', models.CharField(max_length=120)),
                ('cost_center_shortname', models.CharField(max_length=120)),
                ('is_group', models.IntegerField(choices=[(1, 1), (0, 0)], default=0)),
                ('cost_center_group', models.CharField(blank=True, max_length=120)),
                ('created_by', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=120)),
                ('price_list_name', models.CharField(max_length=120)),
                ('is_buying', models.IntegerField(choices=[(1, 1), (0, 0)], default=0)),
                ('is_selling', models.IntegerField(choices=[(1, 1), (0, 0)], default=0)),
                ('is_transfer', models.IntegerField(choices=[(1, 1), (0, 0)], default=0)),
                ('created_by', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusAndRCode',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=120)),
                ('module_group', models.CharField(max_length=120)),
                ('module', models.CharField(max_length=120)),
                ('sub_module', models.CharField(max_length=120)),
                ('trans_type', models.CharField(max_length=120)),
                ('trans_label', models.CharField(max_length=120)),
                ('trans_label_shortname', models.CharField(max_length=120)),
                ('trans_trigger', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=120)),
                ('created_by', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierGroup',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=120)),
                ('supplier_group', models.CharField(max_length=120)),
                ('created_by', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VatGroup',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=120)),
                ('vat_group_name', models.CharField(max_length=120)),
                ('rate', models.CharField(max_length=120)),
                ('created_by', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WithHoldingTaxGroup',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=120)),
                ('wht_name', models.CharField(max_length=120)),
                ('rate', models.CharField(max_length=120)),
                ('created_by', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
