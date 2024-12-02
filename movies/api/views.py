from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from core.models import Movie
from api.serializers import MovieSerializer

class MovieViewSet(ViewSet):
    def list(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response({"list": serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise NotFound("Movie not found")
        serializer = MovieSerializer(movie)
        return Response({"movie": serializer.data}, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = MovieSerializer(data=request.data.get("movie"))
        if serializer.is_valid():
            movie = serializer.save()
            return Response({"movie": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": 400, "reason": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise NotFound("Movie not found")
        serializer = MovieSerializer(movie, data=request.data.get("movie"), partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"movie": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": 400, "reason": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Movie.DoesNotExist:
            raise NotFound("Movie not found")
        except Exception as e:
            return Response({"status": 500, "reason": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
