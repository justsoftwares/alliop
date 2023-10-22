from rest_framework import serializers


def get_serializer(model_class, model_fields='__all__'):
    class ModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = model_class
            fields = model_fields

    return ModelSerializer
