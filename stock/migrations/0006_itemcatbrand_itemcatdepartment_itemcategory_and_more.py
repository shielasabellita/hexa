# Generated by Django 4.0.5 on 2022-06-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_supplieritem_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCatBrand',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=120)),
                ('item_brand', models.CharField(max_length=120)),
                ('created_by', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCatDepartment',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=120)),
                ('item_department', models.CharField(max_length=120)),
                ('created_by', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=120)),
                ('item_category', models.CharField(max_length=120)),
                ('created_by', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCatForm',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=120)),
                ('item_form', models.CharField(max_length=120)),
                ('created_by', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCatManufacturer',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=120)),
                ('item_manufacturer', models.CharField(max_length=120)),
                ('created_by', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCatSection',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=120)),
                ('item_section', models.CharField(max_length=120)),
                ('created_by', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCatSize',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=120)),
                ('item_size', models.CharField(max_length=120)),
                ('created_by', models.CharField(blank=True, max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]