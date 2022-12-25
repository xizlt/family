import json

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from people.models import People


# class DynamicDepthSerializer(serializers.ModelSerializer):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         depth = self.context.get('depth', 0)
#
class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ["first_name", "last_name", "id", "father", "mother"]
        extra_kwargs = {
            'father': {'source': 'father_id'},
            'mother': {'source': 'mother_id'},
        }

class RecursiveField(serializers.ModelSerializer):
    def to_representation(self, value):
        lvalue = self.context.get('depth', None)
        if not lvalue:
            serializer_data = AncestorsSerializer(value, context=self.context).data
            return serializer_data
        if lvalue != 0:
            lvalue -= 1
            self.context.update({'depth': lvalue})
            serializer_data = AncestorsSerializer(value, context=self.context).data
            return serializer_data
        else:
            return f"{value}"

    class Meta:
            model = People
            fields = '__all__'

class AncestorsSerializer(serializers.ModelSerializer):
    mother = RecursiveField(allow_null=True, source="mother_id")
    father = RecursiveField(allow_null=True, source="father_id")

    class Meta:
        model = People
        fields = ["id", "first_name", "last_name", "mother", "father"]