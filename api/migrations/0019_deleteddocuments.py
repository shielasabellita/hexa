# Generated by Django 3.2.9 on 2022-01-15 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20220114_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedDocuments',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('table_name', models.CharField(blank=True, max_length=120)),
                ('id_no', models.CharField(blank=True, max_length=120)),
                ('object', models.CharField(blank=True, max_length=5000)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('deleted_by', models.CharField(max_length=120)),
            ],
        ),
    ]
