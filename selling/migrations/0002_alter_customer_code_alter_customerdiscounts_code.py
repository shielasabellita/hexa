# Generated by Django 4.0.5 on 2022-08-22 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='code',
            field=models.CharField(default='CUST_{9}', max_length=120),
        ),
        migrations.AlterField(
            model_name='customerdiscounts',
            name='code',
            field=models.CharField(default='CUST-DISC_{9}', max_length=120),
        ),
    ]
