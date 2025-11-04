from rest_framework import serializers
from .models import Movies
class Movie_ser(serializers.ModelSerializer):
    class Meta :
        model=Movies
        fields="__all__"