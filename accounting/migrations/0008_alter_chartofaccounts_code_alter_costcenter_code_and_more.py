# Generated by Django 4.0.5 on 2022-08-22 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0007_alter_applyto_code_alter_pricingrule_criteria_amt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartofaccounts',
            name='code',
            field=models.CharField(default='COA_{5}', max_length=120),
        ),
        migrations.AlterField(
            model_name='costcenter',
            name='code',
            field=models.CharField(default='CST-CNTR_{5}', max_length=120),
        ),
        migrations.AlterField(
            model_name='discountgroup',
            name='code',
            field=models.CharField(default='DISC-GRP_{9}', max_length=120),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='code',
            field=models.CharField(default='PR-LST_{5}', max_length=120),
        ),
        migrations.AlterField(
            model_name='pricingrule',
            name='code',
            field=models.CharField(default='PRC-RLE_{6}', max_length=120),
        ),
        migrations.AlterField(
            model_name='suppliergroup',
            name='code',
            field=models.CharField(default='SUP-GRP_{5}', max_length=120),
        ),
        migrations.AlterField(
            model_name='vatgroup',
            name='code',
            field=models.CharField(default='VAT_{5}', max_length=120),
        ),
        migrations.AlterField(
            model_name='withholdingtaxgroup',
            name='code',
            field=models.CharField(default='WTH_{5}', max_length=120),
        ),
    ]