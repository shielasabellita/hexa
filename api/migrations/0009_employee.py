# Generated by Django 3.2.9 on 2022-02-06 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_location_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('emp_code', models.CharField(max_length=120)),
                ('emp_name', models.CharField(max_length=120)),
                ('is_custodian', models.IntegerField(choices=[(1, 1), (0, 0)], default=0)),
                ('is_driver', models.IntegerField(choices=[(1, 1), (0, 0)], default=0)),
                ('employment_type', models.CharField(choices=[('Direct Hire', 'Direct Hire'), ('Agency', 'Agency'), ('Job Order', 'Job Order'), ('On Call', 'On Call')], max_length=120)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=120)),
                ('birthday', models.DateField(blank=True)),
                ('contact_no', models.CharField(blank=True, max_length=120)),
                ('date_of_joining', models.DateField(blank=True)),
                ('date_of_separation', models.DateField(blank=True)),
                ('is_active', models.IntegerField(choices=[(1, 1), (0, 0)], default=0)),
                ('emergency_contact_name', models.CharField(blank=True, max_length=120)),
                ('emergency_contact_no', models.CharField(blank=True, max_length=120)),
                ('relation', models.CharField(blank=True, max_length=120)),
                ('daily_wage', models.CharField(blank=True, max_length=120)),
                ('is_minimum_wage', models.IntegerField(choices=[(1, 1), (0, 0)], default=0)),
                ('cost_center', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.costcenter')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.location')),
            ],
        ),
    ]
