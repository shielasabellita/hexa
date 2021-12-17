# Generated by Django 3.2.9 on 2021-12-17 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50)),
                ('company_shortname', models.CharField(max_length=50)),
                ('company_address', models.CharField(max_length=50, null=True)),
                ('company_contact_no', models.CharField(max_length=50, null=True)),
                ('company_email', models.CharField(max_length=50, null=True)),
                ('is_group', models.BooleanField(default=0)),
                ('company_group', models.CharField(max_length=50, null=True)),
                ('currency', models.CharField(default='PHP', max_length=4)),
                ('company_reg_no', models.CharField(max_length=50, null=True)),
                ('company_taxid_no', models.CharField(max_length=50, null=True)),
                ('business_permit_no', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('deleted_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusAndRCode',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('module_group', models.CharField(max_length=45)),
                ('module', models.CharField(max_length=45)),
                ('sub_module', models.CharField(max_length=45)),
                ('trans_type', models.CharField(max_length=45)),
                ('trans_label', models.CharField(max_length=45)),
                ('trans_label_shortname', models.CharField(max_length=45)),
                ('trans_trigger', models.CharField(max_length=45)),
                ('remarks', models.CharField(max_length=45)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('deleted_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('location_code', models.CharField(max_length=50)),
                ('location_name', models.CharField(max_length=50)),
                ('location_shortname', models.CharField(max_length=50)),
                ('is_group', models.BooleanField(default=0)),
                ('branch_group', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('deleted_at', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
        migrations.CreateModel(
            name='CostCenter',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cost_center_code', models.CharField(max_length=50)),
                ('cost_center_name', models.CharField(max_length=50)),
                ('cost_center_shortname', models.CharField(max_length=50)),
                ('is_group', models.BooleanField(default=0)),
                ('cost_center_group', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('deleted_at', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
        migrations.CreateModel(
            name='ChartOfAccounts',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('account_code', models.CharField(max_length=50)),
                ('account_name', models.CharField(max_length=50)),
                ('coa_group', models.CharField(max_length=50)),
                ('normal_balance', models.CharField(max_length=50)),
                ('report', models.CharField(max_length=50)),
                ('is_default_expense', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('deleted_at', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('branch_code', models.CharField(max_length=45)),
                ('branch_name', models.CharField(max_length=45)),
                ('branch_shortname', models.CharField(max_length=45)),
                ('is_group', models.BooleanField(default=0)),
                ('company_group', models.CharField(max_length=45)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('deleted_at', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
        migrations.CreateModel(
            name='AccountingPeriod',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('acctng_period_code', models.CharField(max_length=45)),
                ('acctng_period_name', models.CharField(max_length=45)),
                ('acctng_period_start_date', models.DateField()),
                ('acctng_period_end_date', models.DateField()),
                ('status', models.CharField(default='Open', max_length=45)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('deleted_at', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
    ]
