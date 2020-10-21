from rest_framework import serializers 

from .models import Genre, Catigories, Title


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Genre


class CatigoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Catigories


class TitleSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Title
