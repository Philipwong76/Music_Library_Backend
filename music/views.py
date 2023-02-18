from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MusicSerializer
from .models import Song

@api_view(['GET', 'POST'])
def song_list(request):
    if request.method == 'GET':
        music = Song.objects.all()
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def song_detail(request, pk):
    try:
        song = Song.objects.get(pk=pk)
        serializer = MusicSerializer(song);
        return Response(serializer.data)
        
    except Song.DoesNotExist:    
        return Response(status=status.HTTP_404_NOT_FOUND);