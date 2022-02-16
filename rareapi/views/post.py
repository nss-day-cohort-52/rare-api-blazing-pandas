from unicodedata import category
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from rareapi.models import Post
from rareapi.models.rareuser import RareUser
from rareapi.models.category import Category

class PostView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data)


    def create(self, request):
        user_id = RareUser.objects.get(user=request.auth.user)
        category = Category.objects.get(pk=request.data['category_id'])
        try:
            serializer = CreatePostSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user_id=user_id, category_id=category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
            
    

       
class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Post
        fields = ('__all__')
        depth = 2
        
class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content']
