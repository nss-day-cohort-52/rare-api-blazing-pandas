from rareapi.models import Category
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

class CategoryView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game
        
        Returns:
            Response -- JSON serialized game
        """
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist as exception:
            return Response({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    """
    class Meta:
        model = Category
        fields = ('id', 'label')