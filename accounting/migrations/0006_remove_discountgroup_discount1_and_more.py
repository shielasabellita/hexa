# Generated by Django 4.0.5 on 2022-07-13 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0005_auto_20220525_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discountgroup',
            name='discount1',
        ),
        migrations.RemoveField(
            model_name='discountgroup',
            name='discount2',
        ),
        migrations.RemoveField(
            model_name='discountgroup',
            name='discount3',
        ),
        migrations.AddField(
            model_name='discountgroup',
            name='discounts',
            field=models.CharField(default='[0]', max_length=120),
            preserve_default=False,
        ),
    ]