from rest_framework import serializers
from .pricing_rule_model import PricingRule

class PricingRuleSerializer(serializers.Serializers):
    class Meta:
        model = PricingRule
        fields = "__all__"