from typing import Tuple
from django.db import models


GLOBAL_YES_NO = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )


class UOM(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    uom = models.CharField(max_length=120)
    must_be_a_whole_number = models.CharField(max_length=120, choices=GLOBAL_YES_NO, default="No")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class ItemCatBrand(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_brand = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class ItemCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_category = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class ItemCatDepartment(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_department = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class ItemCatForm(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_form = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class ItemCatManufacturer(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_manufacturer = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class ItemCatSection(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_section = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class ItemCatSize(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_size = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
