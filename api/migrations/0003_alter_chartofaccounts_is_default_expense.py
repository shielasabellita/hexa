# Generated by Django 3.2.9 on 2021-12-26 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211226_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartofaccounts',
            name='is_default_expense',
            field=models.BooleanField(max_length=120),
        ),
    ]
