"""View module for handling requests about rareusers"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import RareUser
from django.contrib.auth.models import User


class RareUserView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game
        
        Returns:
            Response -- JSON serialized game
        """
        try:
            rareUser = RareUser.objects.get(pk=pk)
            serializer = RareUserSerializer(rareUser)
            return Response(serializer.data)
        except RareUser.DoesNotExist as exception:
            return Response({'message': exception.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """
        rareUsers = RareUser.objects.all().order_by('user__username')
        # rareUser_type = request.query_params.get('type', None)
        # if rareUser_type is not None:
        #     rareUsers = rareUsers.filter(rareUser_type_id=rareUser_type)
        serializer = RareUserSerializer(rareUsers, many=True)
        return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', "user_permissions","groups","is_superuser")

class RareUserSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    user = UserSerializer()
    class Meta:
        model = RareUser
        fields = ('id', 'bio', 'user', 'profile_image_url')
        