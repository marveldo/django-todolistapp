from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer,Task,Profileserializer,Profile


@api_view(['GET'])
def getroutes(request):
    routes =[
        {'GET': 'api/Tasks/' },
        {'GET': 'api/Task/Taskid'}
    ]
    return Response(routes)

@api_view(['GET'])
def Gettasks(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many = True)

    return Response(serializer.data)
@api_view(['GET'])
def getprofiles(request):
    profiles = Profile.objects.all()
    serializer = Profileserializer(profiles, many = True)
    return Response(serializer.data)
@api_view(['GET'])
def Gettask(request,pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(task , many = False)
    return Response(serializer.data)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Createtask(request):
    data = request.data
    print(data)
    name = data['name']
    description = data['description']
    print(name,description)
    Task.objects.create(
        profile = request.user.profile,
        name = name,
        description = description,
        
     )
    
    return Response('Task created')
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def Task_delete(request):
    data = request.data
    Taskid = data['taskid']
    action = data['action']
    task = Task.objects.get(id = Taskid , profile = request.user.profile)
    if action =='delete':
        task.delete()
    return Response('Task deleted')
    