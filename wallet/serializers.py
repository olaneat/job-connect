from rest_framework import serializers 


class BVNSerializer(serializers.Serializer):
    bvn = serializers.CharField(max_length=250)
    