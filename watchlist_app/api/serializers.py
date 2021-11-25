from rest_framework import serializers
from watchlist_app.models import Watchlist, StreamPlatform

class WatchlistSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Watchlist
        fields = "__all__"
    
    def get_len_name(self,object):
        length = len(object.title)
        return length

class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchlistSerializer(many=True, read_only=True)
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movie-detail'
        
        )

    class Meta:
        model = StreamPlatform
        fields = '__all__'