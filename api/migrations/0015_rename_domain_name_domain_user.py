# Generated by Django 3.2.9 on 2022-01-09 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_domain_domain'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domain',
            old_name='domain_name',
            new_name='user',
        ),
    ]
