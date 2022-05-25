from rest_framework import serializers
from .pricing_rule_model import PricingRule

class PricingRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingRule
        fields = "__all__"