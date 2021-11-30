from django.db import models
from django.db.models import fields
from rest_framework import serializers
from watchlist_app.models import Review, Watchlist, StreamPlatform

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('watchlist',)

        

class WatchlistSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')

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