from rest_framework import serializers
from watchlist_app.models import Watchlist, StreamPlatform

class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = '__all__'

class WatchlistSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Watchlist
        fields = "__all__"
    
    def get_len_name(self,object):
        length = len(object.title)
        return length

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Title and description should be different')
        else:
            return data
    
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short!')
        else:
            return value

