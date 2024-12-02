from rest_framework import serializers
from core.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'director', 'length', 'rating']

    def validate_year(self, value):
        if not (1900 <= value <= 2100):
            raise serializers.ValidationError("Year should be between 1900 and 2100.")
        return value

    def validate_rating(self, value):
        if not (0 <= value <= 10):
            raise serializers.ValidationError("Rating should be between 0 and 10.")
        return value
