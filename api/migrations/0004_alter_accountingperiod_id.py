# Generated by Django 3.2.9 on 2021-12-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_chartofaccounts_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountingperiod',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
