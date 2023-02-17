from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer
from .models import Song

@api_view(['GET'])
def song_list(request):

    music = Song.objects.all()

    serializer = MusicSerializer(music, many=True)

    return Response(serializer.data)