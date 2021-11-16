from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from acounts.serializers import UserSerializer

from rest_framework.authtoken.models import Token



# this is a test function
@api_view(["GET", "POST"]) # tells django that this is a type of rest view
def hello_world(request):

    if request.method == 'POST':
        return Response({'message': 'Post request-Response'}, status=status.HTTP_201_CREATED)

    return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)

@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request):
    content = { 'user': str(request.user), 'auth': str(request.auth), }
    return Response(content)

@api_view(['POST'])
def register(request,**prams):
    # first_name= request.POST[prams.get('first_name')]
    # last_name = request.POST[prams.get('last_name')]
    # email = request.POST[prams.get('email')]
    # username = request.POST[prams.get('username')]
    # password= request.POST[prams.get('password')]
    # password2= request.POST[prams.get('password2')]
    serializedUser=UserSerializer(data=request.data)
    if serializedUser.is_valid():
        serializedUser.save()
    else:
        return Response(data=serializedUser.errors,status=status.HTTP_400_BAD_REQUEST)

    data={
        'firstname': serializedUser.data.get('first_name'),
        'token' : Token.objects.get(user__username=serializedUser.data.get('username')).key,
        'id': serializedUser.data.get('id')
    }
    return Response(data=data,status=status.HTTP_201_CREATED)