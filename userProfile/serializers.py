from rest_framework import serializers 
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from .models import UserProfile
from register.models import CustomUser

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    uuid= serializers.UUIDField(format='hex_verbose', source="user.id", read_only=True)
    queryset = UserProfile.objects.all()
    parser_classes = (
        MultiPartParser,
        FormParser
    )

    class Meta:
        model = UserProfile
        fields = (
            'username', 
            'uuid',
            'skills',
            'educationLevel', 
            'displayPicture',
            'email',
            'phoneNumber',
            'ninNumber',
            'countryBase',
            'firstName',
            'surname',
            'subSkills',
            'dateOfBirth',
            'categories'
        )
    def create(self, validated_data, instance=None):
        if 'user' in validated_data:
            user = validated_data.pop('user')
        else:
            user = CustomUser.objects.create(**validated_data)
        profile = UserProfile.objects.update_or_create(
            user=user, defaults=validated_data
        )
        return profile
