from django.urls import path, include
# from watchlist_app.api.views import movie_list,movie_details
from watchlist_app.api.views import WatchDetailAV,WatchListAV,StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie_detail'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream_detail'),
]
 