from typing import Tuple
from django.db import models

# Create your models here.

GLOBAL_YES_NO = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )


# class Item(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     item_code = models.CharField(max_length=120)
#     sku_code = models.CharField(max_length=120)
#     item_barcode = models.CharField(max_length=120)
#     item_name = models.CharField(max_length=120)
#     item_shortname = models.CharField(max_length=120)
#     item_group = models.CharField(max_length=120)
#     is_fixed_asset = models.CharField(max_length=4, choices=GLOBAL_YES_NO, default='No')
#     fixed_asset_group = models.CharField(max_length=120)
#     vat_group = models.CharField(max_length=120)
#     maintain_stock = is_fixed_asset = models.CharField(max_length=4, choices=GLOBAL_YES_NO, default='No')
    
#     # base_oum = models.CharField(max_length=120)
#     # uom = models.CharField(max_length=120)
#     # conversion_factor = models.IntegerField(max_length=11)
    
#     serial_no = models.CharField(max_length=120)
#     batch_no = models.IntegerField(max_length=120)
#     lot_no = models.IntegerField(max_length=120)
#     expiry = models.DateField(null=True)
    
    
#     supplier = models.CharField(max_length=120)
#     discount_group = models.CharField(max_length=120)


#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True, blank=True)
#     deleted_at = models.DateTimeField(auto_now=True, blank=True)

class UOM(models.Model):
    uom = models.CharField(max_length=120, primary_key=True)
    must_be_a_whole_number = models.CharField(max_length=120, choices=GLOBAL_YES_NO, default="No")
    must_be_a_whole_number = models.CharField(max_length=120, choices=GLOBAL_YES_NO, default="No")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, blank=True)



class ItemCatBrand(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_brand = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, blank=True)


class ItemCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_category = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, blank=True)


class ItemCatDepartment(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_department = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, blank=True)


class ItemCatForm(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_form = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, blank=True)


class ItemCatManufacturer(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_manufacturer = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, blank=True)


class ItemCatSection(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_section = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, blank=True)


class ItemCatSize(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_size = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, blank=True)

