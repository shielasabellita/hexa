# Generated by Django 4.0.4 on 2022-04-16 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusAndRCode',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=120)),
                ('module_group', models.CharField(max_length=120)),
                ('module', models.CharField(max_length=120)),
                ('sub_module', models.CharField(max_length=120)),
                ('trans_type', models.CharField(max_length=120)),
                ('trans_label', models.CharField(max_length=120)),
                ('trans_label_shortname', models.CharField(max_length=120)),
                ('trans_trigger', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=120)),
                ('created_by', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
