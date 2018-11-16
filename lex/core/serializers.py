from rest_framework import serializers
from core.models import Code

class CodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Code
        fields = '__all__'