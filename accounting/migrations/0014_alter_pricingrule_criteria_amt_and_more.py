# Generated by Django 4.1.1 on 2022-11-02 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0013_pricingrule_apply_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricingrule',
            name='criteria_amt',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pricingrule',
            name='discount_amt',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
