# Generated by Django 3.2.9 on 2022-01-22 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20220122_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='default_cos_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_cos_account', to='api.chartofaccounts'),
        ),
        migrations.AlterField(
            model_name='item',
            name='default_income_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_income_account', to='api.chartofaccounts'),
        ),
        migrations.AlterField(
            model_name='item',
            name='fixed_asset_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fixed_asset_group', to='api.itemgroup'),
        ),
        migrations.AlterField(
            model_name='item',
            name='vat_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vat_group', to='api.vatgroup'),
        ),
    ]
