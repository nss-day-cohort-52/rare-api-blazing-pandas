from rareapi.models import Tag
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

class TagView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game
        
        Returns:
            Response -- JSON serialized game
        """
        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag)
            return Response(serializer.data)
        except Tag.DoesNotExist as exception:
            return Response({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """
        tags = Tag.objects.all().order_by('label')
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized tag instance
        """
        tag = Tag.objects.create(
            label=request.data["label"],
        )
        serializer = TagSerializer(tag)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        tag.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        """Handle PUT requests for a tag

        Returns:
            Response -- Empty body with 204 status code
        """

        tag = Tag.objects.get(pk=pk)
        tag.label = request.data["label"]
        tag.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    """
    class Meta:
        model = Tag
        fields = ('id', 'label')