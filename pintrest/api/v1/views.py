
from rest_framework.response import Response
from rest_framework import status
from pintrest.models import Movie,Actor
from pintrest.api.v1.serializers import MovieSerializer,ActorSerializer
from rest_framework.decorators import api_view,permission_classes,authentication_classes

from rest_framework.permissions import IsAuthenticated,BasePermission


class UserCanDeleteMovie(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name= 'can-delete').exists():
            return True
        return False

# this is a test function
@api_view(["GET", "POST"]) # tells django that this is a type of rest view
def hello_world(request):

    if request.method == 'POST':
        return Response({'message': 'Post request-Response'}, status=status.HTTP_201_CREATED)

    return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)


@api_view(["GET"])
def movie_index(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def all_actors(request):
    actors = Actor.objects.all()
    serializer = ActorSerializer(instance=actors, many=True)
    print(serializer)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def movie_create(request):
    # print(request.POST)
    serializedmovie=MovieSerializer(data=request.POST)

    if serializedmovie.is_valid():

        serializedmovie.save()
        the_response_data={
            'message':'Succes',
            'data': {'id': serializedmovie.data.get('id')}
        }
    else:
        return Response(data=serializedmovie.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(data=the_response_data, status=status.HTTP_200_OK)

@api_view(['GET'])

def movie_details(request,**prams):
    try:
        mymovie= Movie.objects.get(pk= prams.get('id'))
    except Exception as e:
        return Response(data={'message':'movie doesnt exist'}, status=status.HTTP_200_OK)
    print(mymovie)
    serializedmovie=MovieSerializer(instance=mymovie)

    return Response(data=serializedmovie.data, status=status.HTTP_200_OK)
# the bounus part
@api_view(['GET'])
def movie_actors(request,**prams):
    try:
        mymovie= Movie.objects.get(pk= prams.get('id'))
    except Exception as e:
        return Response(data={'message':'movie doesnt exist'}, status=status.HTTP_200_OK)
    print(mymovie)
    serializedmovie=MovieSerializer(instance=mymovie)

    return Response(data=serializedmovie.data.get('actors'), status=status.HTTP_200_OK)

@api_view(['PATCH', 'PUT'])
def movie_edit(request,**prams):
    try:
        mymovie= Movie.objects.get(pk= prams.get('id'))
    except Exception as e:
        return Response(data={'message':'movie doesnt exist'}, status=status.HTTP_200_OK)

    if request.method=='PUT':
        serializedmovie = MovieSerializer(instance=mymovie,data=request.data,partial=True)
    elif request.method=='PATCH':
       serializedmovie = MovieSerializer(instance=mymovie,data=request.data,partial=True)

    if serializedmovie.is_valid():
        serializedmovie.save()
    else:
        return Response(data={'message':'data is incorrect'}, status=status.HTTP_200_OK)

    return Response(data=serializedmovie.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([UserCanDeleteMovie])
def movie_delete(request,**prams):
    try:
        mymovie= Movie.objects.get(pk= prams.get('id'))
    except Exception as e:
        return Response(data={'message':'movie doesnt exist'}, status=status.HTTP_400_BAD_REQUEST)
    print(mymovie)
    mymovie.delete()
    return Response(data={'movie {} deleted succesfully'.format(mymovie.name)}, status=status.HTTP_200_OK)
