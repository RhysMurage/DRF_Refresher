from django.db import models
from django.db.models import fields
from rest_framework import serializers
from watchlist_app.models import Review, Watchlist, StreamPlatform

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class WatchlistSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Watchlist
        fields = "__all__"
    
    def get_len_name(self,object):
        length = len(object.title)
        return length

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchlistSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"