# Generated by Django 3.2.9 on 2021-12-17 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211217_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartofaccounts',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
