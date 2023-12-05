from rest_framework import serializers
from .item_receipt_model import ItemReceipt

class ItemReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemReceipt
        fields = "__all__"


    def validate(self, data): 
        po_before = ItemReceipt.objects.get(id=data['id'])
        if (po_before.docstatus == 1 and data['docstatus'] == 1):
            raise serializers.ValidationError({"error": "{}: Cannot update when document is already submitted".format(po_before.code)})
        elif po_before.docstatus == 2: 
            raise serializers.ValidationError({"error": "{}: Cannot update cancelled document".format(po_before.code)})
        
        return data
    

    def update(self, instance, validated_data):
        status = {
            0: "Draft",
            1: "Submitted",
            2: "Cancelled"
        }
        instance.status = status[validated_data.get("docstatus")]
        instance.docstatus = validated_data.get("docstatus")
        instance.save()
        return instance